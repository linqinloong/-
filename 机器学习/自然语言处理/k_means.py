from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
# from data_utils import *
import jieba
import matplotlib.pyplot as plt
import warnings


def k_means():
    warnings.filterwarnings("ignore")
    # bigram分词
    segment_bigram = lambda text: " ".join(
        [word + text[idx + 1] for idx, word in enumerate(text) if idx < len(text) - 1])
    # 结巴中文分词
    segment_jieba = lambda text: " ".join(jieba.cut(text))

    '''
        1、加载语料
    '''
    corpus = []
    # corpus = open("del_stop_word_f.txt", "r", encoding="unicode_escape")
    corpus = open("del_space_f.txt", "r", encoding="unicode_escape")

    '''
    '''
    #    2、计算tf-idf设为权重

    vectorizer = CountVectorizer()
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))

    '''
        3、获取词袋模型中的所有词语特征
        如果特征数量非常多的情况下可以按照权重降维
    '''

    word = vectorizer.get_feature_names_out()
    print("word feature length: {}".format(len(word)))

    '''
        4、导出权重，到这边就实现了将文字向量化的过程，矩阵中的每一行就是一个文档的向量表示
    '''
    tfidf_weight = tfidf.toarray()

    '''
        5、对向量进行聚类
    '''

    # 指定分成5个类
    kmeans = KMeans(n_clusters=5) # 多次尝试后n_clusters 300-310之间最好
    kmeans.fit(tfidf_weight)

    # 打印出各个族的中心点
    print(kmeans.cluster_centers_)
    for index, label in enumerate(kmeans.labels_, 1):
        print("index: {}, label: {}".format(index, label))

    # 样本距其最近的聚类中心的平方距离之和，用来评判分类的准确度，值越小越好
    # k-means的超参数n_clusters可以通过该值来评估
    print("inertia: {}".format(kmeans.inertia_))

    '''
        6、可视化
    '''

    # 使用T-SNE算法，对权重进行降维，准确度比PCA算法高，但是耗时长
    tsne = TSNE(n_components=2)
    decomposition_data = tsne.fit_transform(tfidf_weight)

    x = []
    y = []

    for i in decomposition_data:
        x.append(i[0])
        y.append(i[1])

    fig = plt.figure(figsize=(10, 10))
    ax = plt.axes()
    plt.scatter(x, y, c=kmeans.labels_, marker="x")
    plt.xticks(())
    plt.yticks(())
    # plt.show()   #此行测试用，不注释掉保存图片时会是空白
    plt.savefig('k-means.png')
