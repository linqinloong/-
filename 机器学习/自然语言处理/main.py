import re
import pandas as pd
import fileinput

import csv_analyse
import data
import GUI
import LDA
import draw
import path
import TFIDF
import k_means
import MingCiTiQu
import CiXingBiaoZhu
import jieba_analyse

# 注意！在运行main.py前要先执行josn_file_transform_csv_file.py，生成文件news2016zh_valid.csv。为的是json转csv。
# 生成news2016zh_valid.csv后即可运行main.py

# 因发现在运行时出现numpy.core._exceptions.MemoryError错误，内存不够，改了参数内存占用到了百分之九十九还是不够，所以减少文本数量。
# csv转成可用原始数据集

# eccel打开csv文件会乱码因为excel打开csv文件默认是utf-8-bom编码，但是我是utf-8编码，所以可用notepad来正常显示.csv文件，而不用Excel打开。


# 生成data.csv
data.original_data_transform_data_csv()

# 读数据
data_original = data.load_data()
# 数据预处理(删除无效列，删除重复行)
data_preprocessing = data.preprocessing_data(data_original)
# 取出content
data_content = data.select_content(data_preprocessing)  # 输出content_first.txt
# 正则表达式去除数字和英文字母
data.re_del_num_english_word()  # 输入content_first.txt 输出content_del_num_english_word.txt
# 去掉空行
data.del_empty_row()  # 输入content_del_num_english_word.txt 输出content.txt 还有，不去空行的话后面百度api items找不到会报错的。
# 外部载入
f = open('content.txt', encoding='utf-8').read()
# print(f.read())
# jieba_analyse.cut(f)
# 载入自定义词典
jieba_analyse.custom_dictionary()
# 分词
cut_word = jieba_analyse.cut(f)  # add_space_f.txt
# 载入停用词
stop_word = jieba_analyse.stop_word()
# 去停用词
del_stop_word = jieba_analyse.del_stop_word(cut_word, stop_word)  # del_stop_word_f.txt
# 去空格
del_space = jieba_analyse.del_space(del_stop_word)  # del_space_f.txt
# 词频统计
# 统计前十个个出现次数最多的字
top_num_word = jieba_analyse.top_num_word(del_space)
# 词性标注
# 名词提取且统计每个名词的个数
MingCiTiQu.MingCiTiQu()  # 输入的文件是del_space_f.txt 输出在屏幕上
# 关键字提取  csv_analyse里已实现
csv_analyse.csv_analyse(k=100)  # k是选择第几个文本进行关键字提取，并打印在屏幕上。
# Tf-idf：看词的重要程度
TFIDF.tf_idf()
# 词性标注
CiXingBiaoZhu.CiXingBiaoZhu()  # 输入的文件是del_space_f.txt 输出文件是CiXingBiaoZhu.txt
# 主题提取 LDA主题模型 提取主题概率分布
LDA.LDA()   # 生成lda.xlsx
# 词云图
draw.word_cloud()  # 输入的文件是del_space_f.txt，生成ciyun.png
# 情感分析
import sentiment_analysis

sentiment_analysis.sentiment_analyssis()  # 输入的文件是content.txt 输出的文件是sentiments_score_file.txt,输出各行文本的情感值，越靠近1越好。
# GUI
# k-means
k_means.k_means()  # 输入del_stop_word_f.txt，输出显示在屏幕上并生成图片k-means.png

"""def main():
    data = data.load_data()
    data_preprocessing = data.preprocessing_data(data)
    data_preprocessing = data.preprocessing_data(data)


if __name__ == '__main__':
    main()
"""
