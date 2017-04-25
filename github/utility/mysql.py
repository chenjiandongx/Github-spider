import csv
import pymysql

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
    """ 导入爬出仓库数据到数据库 """

    with open(r"e:\python\github\data\repostar.csv", "r", encoding="utf-8") as f:
        data = csv.reader(f)

        def insert_db(repo, repo_fork, repo_star, repo_watch):

            sql = "insert into repostar(repo, repo_fork, repo_star, repo_watch) " \
                  "values(%s, %s, %s, %s)"
            value = (repo, repo_fork, repo_star, repo_watch)
            cur.execute(sql, value)
            conn.commit()
            print("Insert repo: " + repo)

        for index, value in enumerate(data):
            if index > 0:
                repo, repo_fork, repo_star, repo_watch = value
                try:
                    insert_db(repo, repo_fork, repo_star, repo_watch)
                except Exception as e:
                    print(e)


def import_user_data():
    """ 导入爬出用户数据到数据库 """

    with open(r"e:\python\github\data\userdata1.csv", "r", encoding="utf-8") as f:
        data = csv.reader(f)

        def insert_db(user, user_repo, user_star, user_follower, user_following):

            sql = "insert into userdata(user, user_repo, user_star, user_follower, user_following) " \
                  "values(%s, %s, %s, %s, %s)"
            value = (user, user_repo, user_star, user_follower, user_following)
            cur.execute(sql, value)
            conn.commit()
            print("Insert user: " + user)

        for index, value in enumerate(data):
            if index > 0:
                user, user_repo, user_star, user_follower, user_following = value
                try:
                    insert_db(user, user_repo, user_star, user_follower, user_following)
                except Exception as e:
                    print(e)


if __name__ == "__main__":
    import_repo_data()