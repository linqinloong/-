from sklearn import tree
from sklearn.datasets import load_iris
import pydotplus #引入pydotplus

iris = load_iris()# 从sklearn 数据集中获取鸢尾花数据。
X = iris.data
Y = iris.target
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)
dot_data = tree.export_graphviz(clf, out_file=None)
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_pdf("iris.pdf")#将图写成pdf文件