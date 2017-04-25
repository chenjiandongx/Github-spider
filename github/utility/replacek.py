import csv

# 爬出数据 1000 用 k 表示的，要换回整数
with open(r"e:\python\github\data\userdata.csv", "r") as f:
    reader = csv.reader(f)

    # csv 文件的第 column 列
    column = 2
    for index, value in enumerate(reader):
        if index > 0:
            if value[column][-1] == "k":
                try:
                    r = value[column][:-1]
                    print(int(float(r) * 1000))
                except Exception as e:
                    pass
            else:
                print(value[column])
