# 这里我们使用make_regression生成回归模型数据。几个关键参数有n_samples（生成样本数），
# n_features（样本特征数），noise（样本随机噪音）和coef（是否返回回归系数）。
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
from sklearn.datasets.samples_generator import make_regression, make_blobs, make_gaussian_quantiles
from sklearn.datasets.samples_generator import make_classification
# 回归模型随机数据
def logicData():
    # X为样本特征，y为样本输出， coef为回归系数，共1000个样本，每个样本1个特征
    X, y, coef =make_regression(n_samples=1000, n_features=1,noise=10, coef=True)
    # 画图
    plt.scatter(X, y,  color='black')
    plt.plot(X, X*coef, color='blue',linewidth=3)
    plt.xticks(())
    plt.yticks(())
    plt.show()


# 分类模型随机数据
def classModel():
    # X1为样本特征，Y1为样本类别输出， 共400个样本，每个样本2个特征，输出有3个类别，没有冗余特征，每个类别一个簇
    X1, Y1 = make_classification(n_samples=400, n_features=2, n_redundant=0,n_clusters_per_class=1, n_classes=3)
    plt.scatter(X1[:, 0], X1[:, 1], marker='o', c=Y1)
    plt.show()

# 聚类模型随机数据
def classGet():
    # X为样本特征，Y为样本簇类别， 共1000个样本，每个样本2个特征，共3个簇，簇中心在[-1,-1], [1,1], [2,2]， 簇方差分别为[0.4, 0.5, 0.2]
    X, y = make_blobs(n_samples=1000, n_features=2, centers=[[-1, -1], [1, 1], [2, 2]], cluster_std=[0.4, 0.5, 0.2])
    plt.scatter(X[:, 0], X[:, 1], marker='o', c=y)
    plt.show()

# 分组正态分布混合数据
def disAll():
    # 生成2维正态分布，生成的数据按分位数分成3组，1000个样本,2个样本特征均值为1和2，协方差系数为2
    X1, Y1 = make_gaussian_quantiles(n_samples=1000, n_features=2, n_classes=3, mean=[1, 2], cov=2)
    plt.scatter(X1[:, 0], X1[:, 1], marker='o', c=Y1)
    plt.show()
logicData()
classModel()
classGet()
disAll()