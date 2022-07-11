import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation


def LDA():
    def txt_to_df(txt):
        cntVector = CountVectorizer()
        cntTf = cntVector.fit_transform(txt)  # 训练，先拟合再transform
        lda = LatentDirichletAllocation(n_components=TOPIC_NUM,
                                        learning_offset=50.,  # 浮点数，权重
                                        random_state=0)
        lda.fit_transform(cntTf)
        lda_topics = lda.components_ / lda.components_.sum(axis=1)[:, np.newaxis]
        topics = []
        for topic_idx, topic in enumerate(lda_topics):
            t = []
            ll = list(map(lambda i: (cntVector.get_feature_names_out()[i], topic[i]), list(topic.argsort()[:-11:-1])))
            for pair in ll:
                t.append(pair[0] + ' ' + str(float('%.8f' % pair[1])))
            topics.append(t)

        df = pd.DataFrame(topics)
        return df

    ###########################################################
    FILE_TXT = 'del_space_f.txt'
    FILE_WRITE = 'lda.xlsx'
    TOPIC_NUM = 50  # 主题数

    with open(FILE_TXT, encoding='utf-8') as f:
        text = f.readlines()

    t = txt_to_df(np.array(text))
    t.to_excel(FILE_WRITE)
