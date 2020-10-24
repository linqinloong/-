from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
from math import log
import operator
import pickle

#相亲决策树的生成
#属性标注：
#漂亮：0代表不漂亮，1代表漂亮
#钱：0代表没钱，1代表有钱
#约会：0代表不去约会，1代表去约会
def data():
    dataset = [[1,1,1],
               [0,1,0],
               [1,1,1],
               [1,0,0],
               [0,0,0],
               [1,0,0],
               [1,1,1],
               [0,0,0],
               [0,0,0],
               [0,1,0]]
    labels = ['不约会','约会']   #分类属性
    return  dataset,labels      #返回数据集和分类属性

def calcshannonent(dataset):            #计算香农熵
    numentires = len(dataset)
    labelcounts = {}    #统计标签（label）出现的次数（字典类型）
    for featVec in dataset:  # 对每组特征向量进行统计
        currentlabel = featVec[-1]  # 提取标签(Label)信息
        if currentlabel not in labelcounts.keys():  # 如果标签(Label)没有放入统计次数的字典,添加进去
            labelcounts[currentlabel] = 0
        labelcounts[currentlabel] += 1  # Label计数
    shannonent = 0.0  # 经验熵(香农熵)
    for key in labelcounts:  # 计算香农熵
        prob = float(labelcounts[key]) / numentires  # 选择该标签(Label)的概率
        shannonent -= prob * log(prob, 2)  # 利用公式计算
    return shannonent  # 返回经验熵(香农熵)

def splitDataSet(dataSet, axis, value):                 #用来选择各个特征的子集
    retDataSet = []                                        #创建返回的数据集列表
    for featVec in dataSet:                             #遍历数据集
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]                #去掉axis特征
            reducedFeatVec.extend(featVec[axis+1:])     #将符合条件的添加到返回的数据集
            retDataSet.append(reducedFeatVec)
    return retDataSet                                      #返回划分后的数据集

def chooseBestFeatureToSplit(dataset):                  #选择最优特征
    numFeatures = len(dataset[0]) - 1                    #特征数量
    baseEntropy = calcshannonent(dataset)                 #计算数据集的香农熵
    bestInfoGain = 0.0                                  #信息增益
    bestFeature = -1                                    #最优特征的索引值
    for i in range(numFeatures):                         #遍历所有特征
        #获取dataSet的第i个所有特征
        featList = [example[i] for example in dataset]
        uniqueVals = set(featList)                         #创建set集合{},元素不可重复
        newEntropy = 0.0                                  #经验条件熵
        for value in uniqueVals:                         #计算信息增益
            subDataSet = splitDataSet(dataset, i, value)         #subDataSet划分后的子集
            prob = len(subDataSet) / float(len(dataset))           #计算子集的概率
            newEntropy += prob * calcshannonent(subDataSet)    #根据公式计算经验条件熵
        infoGain = baseEntropy - newEntropy                     #信息增益
        print("第%d个特征的增益为%.3f" % (i, infoGain))            #打印每个特征的信息增益
        if (infoGain > bestInfoGain):                             #计算信息增益
            bestInfoGain = infoGain                             #更新信息增益，找到最大的信息增益
            bestFeature = i                                     #记录信息增益最大的特征的索引值
    return bestFeature                                             #返回信息增益最大的特征的索引值

def majorityCnt(classList):                             #统计classList中出现此处最多的元素(类标签)
    classCount = {}
    for vote in classList:  # 统计classList中每个元素出现的次数
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)  # 根据字典的值降序排序
    return sortedClassCount[0][0]  # 返回classList中出现次数最多的元素

def createTree(dataSet, labels, featLabels):        #创建决策树
    classList = [example[-1] for example in dataSet]  # 取分类标签(是否放贷:yes or no)
    if classList.count(classList[0]) == len(classList):  # 如果类别完全相同则停止继续划分
        return classList[0]
    if len(dataSet[0]) == 1 or len(labels) == 0:  # 遍历完所有特征时返回出现次数最多的类标签
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)  # 选择最优特征
    bestFeatLabel = labels[bestFeat]  # 最优特征的标签
    featLabels.append(bestFeatLabel)
    myTree = {bestFeatLabel: {}}  # 根据最优特征的标签生成树
    del (labels[bestFeat])  # 删除已经使用特征标签
    featValues = [example[bestFeat] for example in dataSet]  # 得到训练集中所有最优特征的属性值
    uniqueVals = set(featValues)  # 去掉重复的属性值
    for value in uniqueVals:  # 遍历特征，创建决策树。
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels, featLabels)

    return myTree

def classify(inputTree, featLabels, testVec):
	firstStr = next(iter(inputTree))														#获取决策树结点
	secondDict = inputTree[firstStr]														#下一个字典
	featIndex = featLabels.index(firstStr)
	for key in secondDict.keys():
		if testVec[featIndex] == key:
			if type(secondDict[key]).__name__ == 'dict':
				classLabel = classify(secondDict[key], featLabels, testVec)
			else: classLabel = secondDict[key]
	return classLabel

def getNumLeafs(myTree):                                        #获取决策树叶子结点的数目
    numLeafs = 0												#初始化叶子
    firstStr = next(iter(myTree))								#python3中myTree.keys()返回的是dict_keys,不在是list,所以不能使用myTree.keys()[0]的方法获取结点属性，可以使用list(myTree.keys())[0]
    secondDict = myTree[firstStr]								#获取下一组字典
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict':				#测试该结点是否为字典，如果不是字典，代表此结点为叶子结点
            numLeafs += getNumLeafs(secondDict[key])
        else:   numLeafs +=1
    return numLeafs

def getTreeDepth(myTree):                                       #获取决策树的层数
    maxDepth = 0												#初始化决策树深度
    firstStr = next(iter(myTree))								#python3中myTree.keys()返回的是dict_keys,不在是list,所以不能使用myTree.keys()[0]的方法获取结点属性，可以使用list(myTree.keys())[0]
    secondDict = myTree[firstStr]								#获取下一个字典
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict':				#测试该结点是否为字典，如果不是字典，代表此结点为叶子结点
            thisDepth = 1 + getTreeDepth(secondDict[key])
        else:   thisDepth = 1
        if thisDepth > maxDepth: maxDepth = thisDepth			#更新层数
    return maxDepth

if __name__ == '__main__':
    dataset, features = data()
    #print(dataset)
    #print(calcshannonent(dataset))      #香农熵
    #print("最优特征索引值:" + str(chooseBestFeatureToSplit(dataset)))
    featLabels = []
    myTree = createTree(dataset, features, featLabels)
    testVec = [0, 1]  # 测试数据
    result = classify(myTree, featLabels, testVec)
    if result == '1':
        print('约会')
    if result == '0':
        print('不约会')