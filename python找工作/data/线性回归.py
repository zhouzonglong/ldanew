# 线性回归的步骤
# 1.获取数据，定义问题
# 2.整理数据
# 3.用pandas来读取数据
# 4.准备运行算法的数据
# 5.划分训练集和测试集
# 6.运行scikit - learn的线性模型
# 7.模型评价
# 8.交叉验证
# 9.画图观察结果


import matplotlib
import matplotlib.pyplot as plt
# %matplotlib inline
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.model_selection import cross_val_predict

data = pd.read_csv('ccpp.csv')
X = data[['AT', 'V', 'AP', 'RH']]
y = data[['PE']]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
# 6.运行scikit - learn的线性模型
linreg = LinearRegression()
linreg.fit(X_train, y_train)
# print (linreg.intercept_)      #对应A0
# print (linreg.coef_)           #对应A1 A2 A3 A4
# 7.模型评价
y_pred = linreg.predict(X_test)
# 用scikit-learn计算MSE(均方差)
print ("MSE:",metrics.mean_squared_error(y_test, y_pred))
# 用scikit-learn计算RMSE（均方根差）
print ("RMSE:",np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
# 8.交叉验证   十折交叉验证
predicted = cross_val_predict(linreg, X, y, cv=10)
# 用scikit-learn计算MSE
print ("MSE:",metrics.mean_squared_error(y, predicted))
# 用scikit-learn计算RMSE
print ("RMSE:",np.sqrt(metrics.mean_squared_error(y, predicted)))
# 9.画图观察结果
fig, ax = plt.subplots()
ax.scatter(y, predicted)
ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()