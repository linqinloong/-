import random
import csv  # csv包可以读写csv文件

K = 5

# 数据读取
with open('iris.csv', 'r') as file:
    reader = csv.DictReader(file)
    #    for row in reader:
    #        print(row)
    datas = [row for row in reader]

# 分组
random.shuffle(datas)  # 将数据集打乱顺序，相当于洗牌
n = len(datas) // 3  # 整除，避免小数的出现
# 2/3是训练集 1/3是测试集
test_set = datas[0:n]  # 第0个到第n个不包含第n个
train_set = datas[n:]  # 从n开始到最后


def distance(d1, d2):
    res = 0  # 求和
    for key in ('sepal_length', 'sepal_width', 'petal_length', 'petal_width'):
        res += (float(d1[key]) - float(d2[key])) ** 2  # 把每一个对应维度上的数据两两相减  从csv中读取出的都是字符串，因此要转换成数字形式
    return res ** 0.5


def knn(data):
    #        KNN算法过程
    #        1.求距离
    #        2.排序——升序
    #        3.取前K个
    #        4.加权平均

    # 1.求距离
    res = [
        {"result": train['species'], "distance": distance(data, train)}
        for train in train_set
    ]
    # 排序-升序
    res = sorted(res, key=lambda item: item['distance'])
    # 取前K个
    resK = res[0:K]
    #    print(resK)
    # 4.加权平均(离的近的权重高，离得远的权重低)
    result = {'setosa': 0, 'versicolor': 0, 'virginica': 0}
    # 算前K个的总距离
    sum_distance = 0
    for r in resK:
        sum_distance += r['distance']
    for r in resK:
        result[r['result']] += 1 - r['distance'] / sum_distance  # 计算权重
    #    print(result)
    #    print(data['species'])
    return (sorted(result, key=lambda x: result[x])[-1])  # 返回字典中最大value对应的key


correct = 0
for test in test_set:
    result = test['species']  # 真实结果
    result_predict = knn(test)

    if result == result_predict:
        correct += 1

score = correct / len(test_set)
# print(score)
print("test Accuracy:{:.2f}".format(score))
