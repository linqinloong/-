import pandas as pd
import path
import re

data_path = path.data_path


def load_data():
    """加载数据"""
    data = pd.read_csv(data_path)
    # print(data)
    return data


def re_del_num_english_word():
    """正则表达式去除数字和英文字母"""
    for line in open("content_first.txt", encoding='utf-8'):
        write_in = re.sub("[0-9a-zA-Z]", repl='', string=line)
        txt2 = open("content_del_num_english_word.txt", 'a', encoding='utf-8')
        txt2.write(write_in)


def preprocessing_data(data):
    """数据预处理"""
    # 删除无效列
    data = data.drop(['news_id', 'time'], axis=1)
    # 删除重复行
    data = data.drop_duplicates()
    data.to_csv("preprocessing_data.csv", index=False, encoding="utf_8_sig")
    return data


def select_content(data):
    """选择content内的内容"""
    data = data.loc[:, ['content']]
    data.to_csv('content_first.txt', sep='\t', index=False, encoding='utf-8')


def original_data_transform_data_csv():
    data = pd.read_csv('news2016zh_valid.csv', nrows=1000, encoding="utf-8")  # nrows取前多少个数据
    data.to_csv("data.csv", encoding="utf-8")


def del_empty_row():
    """去掉空行"""
    file1 = open('content_del_num_english_word.txt', 'r', encoding='utf-8')  # 要去掉空行的文件
    file2 = open('content.txt', 'w', encoding='utf-8')  # 生成没有空行的文件
    try:
        for line in file1.readlines():
            if line == '\n':
                line = line.strip("\n")
            file2.write(line)
    finally:
        file1.close()
        file2.close()
