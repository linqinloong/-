from collections import Counter  # 计数器


def MingCiTiQu():
    f1 = open("del_space_f.txt", 'r', encoding='utf-8')
    # 构建一个空列表，用以保存提取出的每个词
    words = []
    # 构建一个空列表，用于保存提取出的名词
    ming_words = []
    for i in f1.readlines():
        # print(i.replace('x','').split(" "))
        line = i.split(" ")
        for j in line:
            if (j != '' and j != '\n' and j != 'x'):
                words.append(j)
    # 提取名词
    for i in words:
        # if('n' in i):
        ming_words.append(i)

    # 统计词频
    counter = Counter(ming_words)
    dictionary = dict(counter)

    k = 10  # 数量从多到少排前k个名词
    res = counter.most_common(k)
    print("名词提取且统计每个名词的个数:")
    print(res)
