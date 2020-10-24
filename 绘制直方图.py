import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
mu,sigma = 100,20   #均值和标准差
a =np.random.normal(mu,sigma,size=100)

plt.hist(a,20,histtype='stepfilled',facecolor='b',alpha=0.75)  #有20个直方
plt.title("Histogram")
plt.show()