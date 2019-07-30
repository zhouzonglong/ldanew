import pydotplus
from sklearn.datasets import load_iris
from sklearn import tree
import sys
import os
# 下面用于python找不到graphviz使用
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

# 载入自带数据
iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)

# 保存模型
with open("iris.dot", 'w') as f:
    f = tree.export_graphviz(clf, out_file=f)

# 查看图
# 第二种方法是用pydotplus生成iris.pdf。这样就不用再命令行去专门生成pdf文件了。
# import pydotplus
# dot_data = tree.export_graphviz(clf, out_file=None)
# graph = pydotplus.graph_from_dot_data(dot_data)
# graph.write_pdf("iris.pdf")

# 第三种办法是个人比较推荐的做法，因为这样可以直接把图产生在ipython的notebook。代码如下：
# 在anaconda里面可以生成彩色图片

from IPython.display import Image
dot_data = tree.export_graphviz(clf, out_file=None,
                         feature_names=iris.feature_names,
                         class_names=iris.target_names,
                         filled=True, rounded=True,
                         special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data)
Image(graph.create_png())
