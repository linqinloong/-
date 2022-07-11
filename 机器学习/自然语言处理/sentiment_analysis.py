"""def test_svm(self):
    print("SVMClassifier")
    print("---" * 45)
    print("Train num = %s" % self.train_num)
    print("Test num = %s" % self.test_num)
    print("C = %s" % self.C)

    from classifier import SVMClassifier
    svm = SVMClassifier(self.train_data, self.train_labels, self.best_words, self.C)

    classify_labels = []
    print("SVMClassifier is testing ...")
    for data in self.test_data:
        classify_labels.append(svm.classify(data))
    print("SVMClassifier tests over.")

    filepath = "f_runout/SVM-%s-train-%d-test-%d-f-%d-C-%d-%s-lin.xls" % \
               (self.type,
                self.train_num, self.test_num,
                self.feature_num, self.C,
                datetime.datetime.now().strftime(
                    "%Y-%m-%d-%H-%M-%S"))

    self.write(filepath, classify_labels, 2)"""
"""from snownlp import SnowNLP

# with open("content.txt", "r", encoding='utf-8') as f:  # 打开文件
#    data = f.read()  # 读取文件
# def sentiment_analyssis():
f = open("content.txt", encoding='utf-8')  # 返回一个文件对象
line = f.readline()  # 调用文件的 readline()方法
while line:
    line = f.readline()
    if line == 0:
        line = 1
    else:
        s = SnowNLP(line)

        #print(s.sentiments)  # 情感分数
        sentiments_score = s.sentiments
        sentiments_score_file = open("sentiments_score_file.txt", 'a', encoding='utf-8')
        sentiments_score_file.write(str(sentiments_score))
        sentiments_score_file.write('\r\n')"""

# print(list(s.tags)) # 词性标注(快速)和main里自己写的词性标注不一样
# q = SnowNLP("我非常伤心")
# print(q.sentiments) # 情感分数
# s = SnowNLP(data)
# print(s.keywords(limit=3)) #提取3个关键字
# print(s.sentiments) # 情感分数
"""summary = s.summary(limit=4)    # 提取文本摘要
for i in summary:
    print(i)
"""
# 备注
# TensorFlow和gensim效率高但是我实现总有些问题，所以先采用SnowNLP库完成工程，SnowNLP库效率低，但其中已预训练了模型，可以省很多事。
"""q = SnowNLP("我非常伤心")
print(q.sentiments) # 情感分数"""


def sentiment_analyssis():
    # 百度api更简单，所以换百度api
    import aip
    import time
    import numpy as np
    import pandas as pd
    client_appid = '25658360'
    client_ak = 'CLjUTG77xFP3GoxfvkFTl291'
    client_sk = '58wl1Hc0qHluECADOGIZcL1mROd0xugG'
    nlp = aip.nlp.AipNlp(client_appid, client_ak, client_sk)
    f1 = open("content.txt", encoding='utf-8')
    for i in range(10):  # 为了运行速率，所以只取了前十行
        line = f1.readline().strip()
        line = line[0:200]  # 因为百度api对字符串长度有要求所以输入长度改为200
        # print(nlp.sentimentClassify(line))
        # print(nlp.sentimentClassify(line)['items'][0]['positive_prob'])
        dict_data_positive_prob = nlp.sentimentClassify(line)['items'][0]['positive_prob']
        txt_positive_prob = open("属于积极类别概率.txt", 'a', encoding='utf-8')
        txt_positive_prob.write(str(dict_data_positive_prob))
        txt_positive_prob.write('\r\n')
        time.sleep(0.2)  # 防止'error_code': 18错误，因为百度api对QPS有超额限制。
        dict_data_negative_prob = nlp.sentimentClassify(line)['items'][0]['negative_prob']
        txt_negative_prob = open("属于消极类别概率.txt", 'a', encoding='utf-8')
        txt_negative_prob.write(str(dict_data_negative_prob))
        txt_negative_prob.write('\r\n')
        time.sleep(0.2)  # 防止'error_code': 18错误，因为百度api对QPS有超额限制。
        dict_data_sentiment = nlp.sentimentClassify(line)['items'][0]['sentiment']
        txt_sentiment = open("情感极性分类结果0负向1中性2正向.txt", 'a', encoding='utf-8')
        txt_sentiment.write(str(dict_data_sentiment))
        txt_sentiment.write('\r\n')
        time.sleep(0.2)  # 防止'error_code': 18错误，因为百度api对QPS有超额限制。
        dict_data_confidence = nlp.sentimentClassify(line)['items'][0]['confidence']
        txt_confidence = open("分类的置信度.txt", 'a', encoding='utf-8')
        txt_confidence.write(str(dict_data_confidence))
        txt_confidence.write('\r\n')
        time.sleep(0.2)  # 防止'error_code': 18错误，因为百度api对QPS有超额限制
    # sentiment	int	表示情感极性分类结果，0:负向，1:中性，2:正向
    # confidence	float	表示分类的置信度，取值范围[0,1]
    # positive_prob	float	表示属于积极类别的概率 ，取值范围[0,1]
    # negative_prob	float	表示属于消极类别的概率，取值范围[0,1]
