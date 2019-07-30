import matplotlib.pyplot as plt
# %matplotlib inline
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import Ridge
from sklearn.linear_model import RidgeCV
def getModelRigide():
    data = pd.read_csv('ccpp.csv')
    X = data[['AT', 'V', 'AP', 'RH']]
    y = data[['PE']]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
    #训练模型  指定a=1随机
    # 　PE=θ0+θ1∗AT+θ2∗V+θ3∗AP+θ4∗RH
    ridge = Ridge(alpha=1)
    ridge.fit(X_train, y_train)
    print (ridge.coef_)   #θ1234
    print (ridge.intercept_)#θ0

    #指定一系列a的值，然后选出最优
    ridgecv = RidgeCV(alphas=[0.01, 0.1, 0.5, 1, 3, 5, 7, 10, 20, 100])
    ridgecv.fit(X_train, y_train)
    print(ridgecv.alpha_ )
def get_a_o():
    # X is a 10x10 matrix
    X = 1. / (np.arange(1, 11) + np.arange(0, 10)[:, np.newaxis])
    # y is a 10 x 1 vector
    y = np.ones(10)

    n_alphas = 200
    # alphas count is 200, 都在10的-10次方和10的-2次方之间
    alphas = np.logspace(-10, -2, n_alphas)
    clf = linear_model.Ridge(fit_intercept=False)
    coefs = []
    # 循环200次
    for a in alphas:
        # 设置本次循环的超参数
        clf.set_params(alpha=a)
        # 针对每个alpha做ridge回归
        clf.fit(X, y)
        # 把每一个超参数alpha对应的theta存下来
        coefs.append(clf.coef_)

    ax = plt.gca()
    ax.plot(alphas, coefs)
    # 将alpha的值取对数便于画图
    ax.set_xscale('log')
    # 翻转x轴的大小方向，让alpha从大到小显示
    ax.set_xlim(ax.get_xlim()[::-1])
    plt.xlabel('alpha')
    plt.ylabel('weights')
    plt.title('Ridge coefficients as a function of the regularization')
    plt.axis('tight')
    plt.show()
    # 从图上也可以看出，当α比较大，接近于10−2的时候，θ的10个维度都趋于0。
    # 而当α比较小，接近于10−10的时候，θ的10个维度都趋于线性回归的回归系数。
get_a_o()