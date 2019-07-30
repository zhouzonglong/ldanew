# GaussianNB类使用总结

import numpy as np
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
#拟合数据
clf.fit(X, Y)
print ("==Predict result by predict==")
print(clf.predict([[-0.8, -1]]))
print ("==Predict result by predict_proba==")
print(clf.predict_proba([[-0.8, -1]]))
print ("==Predict result by predict_log_proba==")
print(clf.predict_log_proba([[-0.8, -1]]))
# 从上面的结果可以看出，测试样本[-0.8,-1]的类别预测为类别1。具体的测试样本[-0.8,-1]被预测为1的概率为9.99999949e-01 ，
# 远远大于预测为2的概率5.05653254e-08。这也是为什么最终的预测结果为1的原因了。
# 此外，GaussianNB一个重要的功能是有 partial_fit方法，这个方法的一般用在如果训练集数据量非常大，一次不能全部载入内存的时候。
# 这时我们可以把训练集分成若干等分，重复调用partial_fit来一步步的学习训练集，非常方便。后面讲到的MultinomialNB和BernoulliNB也有类似的功能。
#


# MultinomialNB类使用总结
# BernoulliNB类使用总结
# 用法和上面的一样













