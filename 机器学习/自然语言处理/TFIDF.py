import pandas as pd
import numpy as np
import jieba
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer


def tf_idf():
    def seg_sentence(sentence, stopwords):
        """对句子进行分词，并去除停用词
        Args:
            sentence:句子(str)
            stopwords:停用词List
        Returns:
            outstr:分词并去除停用词的句子(str)
        """
        sentence_seged = jieba.cut(sentence.strip())
        outstr = ''
        for word in sentence_seged:

            if word not in stopwords:
                if word != '\t':
                    outstr += word
                    outstr += ' '
        return outstr

    swPath = 'stop_word.txt'
    f = open(swPath, 'r', encoding='UTF-8')
    lines = f.readlines()
    stopwords = list(map(lambda line: line.strip(),
                         filter(lambda x: x != '', lines)))
    stopwords.append(' ')
    stopwords = list(set(stopwords))
    f.close()

    with open("del_space_f.txt", encoding='UTF-8') as f:
        text = f.readlines()
    seg_text = list(map(lambda review: seg_sentence(review, stopwords), text))

    # CountVectorizer特征数值计算，对于每一个训练文本，它只考虑每种词汇在该训练文本中出现的频率。
    # 构造Ngramc词袋模型,n-gram考虑了词汇出现的先后顺序
    # ngram_range=(1, 3)选取1到3个词作为组合方式
    # max_features，默认为None，可设为int，对所有关键词的词频进行降序排序，只取前max_features个作为关键词集
    ngram_vectorizer = CountVectorizer(ngram_range=(1, 3), max_features=50)

    count = ngram_vectorizer.fit_transform(
        seg_text).toarray()  # 训练，计算各个词语出现次数，toarray集合转数组,看词频矩阵结果，seg_text把所有行全读到了debug可看。
    featureName = ngram_vectorizer.get_feature_names_out()  # 看到所有文本的关键字
    featureName = list(map(lambda vec: vec.replace(' ', '_'), featureName))
    seg_text = []
    # 将此词频矩阵转换为TF—IDF值
    tfidf_transformer = TfidfTransformer()
    word_vec = tfidf_transformer.fit_transform(count).toarray()

    name = np.matrix(featureName)
    final = np.vstack((name, word_vec))
    df = pd.DataFrame(final)

    # 最终特征名称和数据保存在csv文件中
    df.to_csv('TF-IDF.csv', index=False, header=False, encoding='GBK')

    # 备注
    # 每一行是每个文本，每一列是我们提取的50个特征，所以TF-IDF展现的是这50个特征在每一个文本中的重要程度。
