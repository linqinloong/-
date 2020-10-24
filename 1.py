from sklearn import preprocessing
import numpy as np
X = np.array([[3.2,1.78,130.,6000.],
             [3.5,1.76,122.,7000.],
             [3.,1.73,135.,5500.],
             [2.8,1.80,120.,4000.],
             [3.7,1.85,113.,10000.],
             [2.5,1.74,141.,3200.],
             [3.6,1.69,156.,8000.],
             [4.,1.82,178.,9000.],
             [3.3,1.90,114.,15000.],
             [3.2,1.75,160.,6500.]])
X_scaled = preprocessing.scale(X)   #将给定数据标准化
print(X_scaled)
#处理后数据的均值和方差
print(X_scaled.mean(axis=0))    #boolean类型，默认为true，表示将数据均值规范到0
print(X_scaled.std(axis=0))     #boolean类型，默认为true，表示将数据方差规范到1
