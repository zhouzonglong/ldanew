import numpy as np


# numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
#
# 在指定的间隔内返回均匀间隔的数字。
#
# 返回num均匀分布的样本，在[start, stop]。
#
# 这个区间的端点可以任意的被排除在外。
# stike = np.linspace(50, 150, 24)
# ttm = np.linspace(0.5, 2.5, 24)
# stike, ttm = np.meshgrid(stike, ttm)
# print(stike.shape)


# from sklearn.datasets import make_gaussian_quantiles
#
# X1, y1 = make_gaussian_quantiles(cov=2.0,n_samples=20, n_features=2,n_classes=2, random_state=1)
# # 生成2维正态分布，生成的数据按分位数分为两类，400个样本,2个样本特征均值都为3，协方差系数为2
# X2, y2 = make_gaussian_quantiles(mean=(3, 3), cov=1.5,n_samples=30, n_features=2, n_classes=2, random_state=1)
# #讲两组数据合成一组数据
# X = np.concatenate((X1, X2))
# print(X.shape)
# y = np.concatenate((y1, - y2 + 1))
#
# x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
# y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
# xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
#                      np.arange(y_min, y_max, 0.02))
# print(xx.shape)
list=[1,2,3]
print(list.remove(2))
print(len(''))