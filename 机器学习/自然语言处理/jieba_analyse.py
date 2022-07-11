import jieba
import re
import numpy as np
import pandas as pd


def cut(data):
    """分词"""
    data = jieba.lcut(data)
    # 分完的词转回文本（加空格）
    data = ' '.join(data)
    # 保存文本文件
    with open('add_space_f.txt', 'w', encoding='utf-8') as f:
        f.write(data)
    return data


def custom_dictionary():
    """自定义词典"""
    jieba.load_userdict('custom_dictionary.txt')


def stop_word():
    """停用词词典"""
    stopword = []
    with open('stop_word.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            l = line.strip()
            if l == '\\n':  # 换行符
                l = '\n'
            if l == '\\u3000':  # 制表符
                l = '\u3000'

            stopword.append(l)
    return stopword


def del_stop_word(cut_word, stop_word):
    """去停用词"""
    outstr = ''  # 输出结果
    for word in cut_word:
        if word not in stop_word:
            outstr += word
            # outstr += " "
    # 保存文本文件
    with open('del_stop_word_f.txt', 'w', encoding='utf-8') as f:
        f.write(outstr)
    return outstr


"""def del_space_and_one_word():
    #去掉无效数据
    k = []
    lines = open('del_stop_word_f.txt', encoding='utf-8').readlines()  # type(list)
    for i in lines:
        if len(i) > 1:
            k.append(i)
    str = "".join(k)
    # 多空格换成一空格
    str.replace('  ', ' ')
    # 保存文本文件
    with open('del_space_and_one_word.txt', 'w', encoding='utf-8') as f:
        f.write(str)"""


def del_space(data):
    """删除空格"""
    strafter = re.sub(' +', ' ', data)  # 多空格换成单空格，好看。
    # 保存文本文件
    with open('del_space_f.txt', 'w', encoding='utf-8') as f:
        f.write(strafter)
    return strafter


def top_num_word(data):
    """统计字的出现次数"""
    counts = {}  # count空字典
    for word in data:
        counts[word] = counts.get(word, 0) + 1  # 找不到给0,找的到给1，又找到就再加一，从而实现词频统计

    items = list(counts.items())  # 字典里所有键值对变成列表[('好',3),('耶',4)]
    items.sort(key=lambda x: x[1], reverse=True)  # 排序

    print("前十个出现次数最多的字为：")

    # 前十个出现次数最多的字
    for i in range(10):
        word, count = items[i]
        print("{0:<10}{1:5}".format(word, count))
