import re

import numpy
import pandas as pd
import numpy as np
import jieba


def csv_analyse(k):
    # 读数据
    import jieba
    data = pd.read_csv('data.csv', encoding='utf-8')

    # print(data.head(2))
    content = data.content.values.tolist()  # 取值并转成list格式
    # print(content[0])
    # content_1 = data.title.values.tolist()  #取值并转成list格式
    # print(content_1[1])

    content_S = []  # 分完词后的结果存在content_S里
    for line in content:
        current_segmet = jieba.lcut(str(line))
        if len(current_segmet) > 1 and current_segmet != '\r\n':  # 换行符
            content_S.append(current_segmet)
    # print(content_S[0])
    df_content = pd.DataFrame({'content_S': content_S})
    # print(df_content.head(3))
    """    # 停用词表
        stopwords = pd.read_csv("stop_word.txt", index_col=False, sep='\t', quoting=3, names=['stopword'],
                                encoding='utf-8')  # 不设置quoting，默认会去除英文双引号，只留下英文双引号内的内容，设置quoting = 3，会如实读取内容
        #print(stopwords.head(1))
    
    
        def drop_stopwords(contents, stopwords):
            word = []
            contents_clean = []
            all_words = []
            for line in contents:
                line_clean = []
                if word in line:
                    for word in stopwords:  # 只出现在停用词中，过滤掉。没出现在在停用词当中，拿过来
                        continue
                    line_clean.append(word)
                    all_words.append(str(word))  # all_words做词源
                contents_clean.append(line_clean)
            return contents_clean, all_words
    
    
        # 看一下出现了多少个词
        contents = df_content.content_S.values.tolist()
        stopwords = stopwords.stopword.values.tolist()
        contents_clean, all_words = drop_stopwords(contents, stopwords)
    
        # 看当前结果
        df_all_content = pd.DataFrame({'contents_clean':contents_clean})
        df_all_content.head()
    
        df_all_words = pd.DataFrame({'all_words':all_words})
        df_all_words.head()
        # 看词频
        words_count = df_all_words.groupby(by=['all_words'])['all_words'].agg(["count",numpy.size]) # pd库更新了，原:改,原{改[ 之后才能正常运行，真难找QAQ。
        words_count = words_count.reset_index().sort_values(by=["count"],ascending=False)
        words_count.head()"""

    # TF-IDF关键字提取
    import jieba.analyse
    index = k  # 找第几个文本
    # print(df_news['content'][index])
    print("第%d个文本的前5个关键字为：" % index)
    content_S_str = "".join(content_S[index])
    print("  ".join(jieba.analyse.extract_tags(content_S_str, topK=5, withWeight=False)))  # topK是几个关键字
