import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0, 2 * np.pi, 100)
Y = np.sin(X)
plt.plot(X, Y)  # (X,Y)-->画正弦函数
plt.title('正弦函数',fontproperties='SimHei',fontsize=25)
plt.xlabel('横轴X',fontproperties='SimHei',fontsize=15)
plt.ylabel('纵轴Y',fontproperties='SimHei',fontsize=15)
plt.text(1,-0.5,'X:0->7  Y:-1->1',fontsize=10)
plt.show()