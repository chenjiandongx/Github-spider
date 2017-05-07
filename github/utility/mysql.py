import csv
import pymysql
from collections import namedtuple

conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="0303", db="chenx", charset="utf8")
cur = conn.cursor()

# 创建数据库表
"""
create table repostar/repofork(
    repo varchar(255) not null primary key,
    repo_fork int(8),
    repo_star int(8),
    repo_watch int(8)
);

create table userdata(
    user varchar(255) not null primary key,
    user_repo int(8),
    user_star int(8),
    user_follower int(8),
    user_following int(8)
);

"""

def import_repo_data():
    """ 导入爬取仓库数据到数据库 """
    with open(r"e:\python\github\data\repostar.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        headers = next(reader)
        print(headers)

        def insert_db(repo, repo_fork, repo_star, repo_watch):

            sql = "insert into repostar(repo, repo_fork, repo_star, repo_watch) " \
                  "values(%s, %s, %s, %s)"
            value = (repo, repo_fork, repo_star, repo_watch)
            cur.execute(sql, value)
            conn.commit()
            print("Insert repo: " + repo)

        for _, value in enumerate(reader):
            repo, repo_fork, repo_star, repo_watch = value
            try:
                insert_db(repo, repo_fork, repo_star, repo_watch)
            except Exception as e:
                print(e)


def import_user_data():
    """ 导入爬取用户数据到数据库 """
    with open(r"e:\python\github\data\userdata.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        headers = next(reader)
        print(headers)

        def insert_db(user, user_repo, user_star, user_follower, user_following):

            sql = "insert into userdata(user, user_repo, user_star, user_follower, user_following) " \
                  "values(%s, %s, %s, %s, %s)"
            value = (user, user_repo, user_star, user_follower, user_following)
            cur.execute(sql, value)
            conn.commit()
            print("Insert user: " + user)

        for _, value in enumerate(reader):
            user, user_repo, user_star, user_follower, user_following = value
            try:
                insert_db(user, user_repo, user_star, user_follower, user_following)
            except Exception as e:
                print(e)


def replacek():
    """ 爬取数据 1000 用 k 表示的，要换回整数 """
    with open(r"e:\python\github\data\userdata.csv", "r") as f:
        reader = csv.reader(f)
        headers = next(reader)
        # print(headers)
        Row = namedtuple('Row', headers)

        for r in reader:
            row = Row(*r)
            col = row.user_follower
            if col[-1] == "k":
                v = int(float(col[:-1]) * 1000)
                print(v)
            else:
                print(col)


if __name__ == "__main__":
    import_repo_data()