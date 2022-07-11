# -*-coding:utf-8-*-
import csv
import json
import sys
import codecs


def trans(path):
    jsonData = codecs.open(path + '.json', 'r', encoding='utf-8')
    # csvfile = open(path+'.csv', 'w')  # 此处这样写会导致写出来的文件会有空行
    # csvfile = open(path+'.csv', 'wb')  # python2下
    csvfile = open(path + '.csv', 'w', newline='', encoding="utf-8")  # python3下
    writer = csv.writer(csvfile, delimiter=',')
    flag = True
    for line in jsonData:
        dic = json.loads(line)
        if flag:
            # 获取属性列表
            keys = list(dic.keys())
            # print(keys)
            writer.writerow(keys)  # 将属性列表写入csv中
            flag = False
        # 读取json数据的每一行，将values数据一次一行的写入csv中
        writer.writerow(list(dic.values()))
    jsonData.close()
    csvfile.close()


if __name__ == '__main__':
    # path=str(sys.argv[1]) # 获取path参数
    path = r"D:\text_analyse\news2016zh_valid"
    print(path)
    trans(path)

"""import json
import csv
with open(r'D:\新闻语料json版(news2016zh)\news2016zh_valid.json') as json_file:
    jsondata = json.load(json_file)
data_file = open('D:\新闻语料json版(news2016zh)\jsonoutput.csv', 'w', newline='')
csv_writer = csv.writer(data_file)
count = 0
for data in jsondata:
    if count == 0:
        header = data.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(data.values())
data_file.close()"""
