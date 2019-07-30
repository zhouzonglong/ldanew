# 我们使用这些类的时候，如果有经验知道数据是线性可以拟合的，那么使用LinearSVC去分类 或者LinearSVR去回归，它们不需要我们去慢慢的调参去选择各种核函数以及对应参数， 速度也快。如果我们对数据分布没有什么经验，一般使用SVC去分类或者SVR去回归，这就需要我们选择核函数以及对核函数调参了。
# 什么特殊场景需要使用NuSVC分类 和 NuSVR 回归呢？如果我们对训练集训练的错误率或者说支持向量的百分比有要求的时候，可以选择NuSVC分类 和 NuSVR 。它们有一个参数来控制这个百分比。

'''
重点！！！！！！
'''
# 1）一般推荐在做训练之前对数据进行归一化，当然测试集中的数据也需要归一化。。
# 2）在特征数非常多的情况下，或者样本数远小于特征数的时候，使用线性核，效果已经很好，并且只需要选择惩罚系数C即可。
# 3）在选择核函数时，如果线性拟合不好，一般推荐使用默认的高斯核'rbf'。这时我们主要需要对惩罚系数C和核函数参数γ进行艰苦的调参，通过多轮的交叉验证选择合适的惩罚系数C和核函数参数γ。
# 4）理论上高斯核不会比线性核差，但是这个理论却建立在要花费更多的时间来调参上。所以实际上能用线性核解决问题我们尽量使用线性核。

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, svm
from sklearn.svm import SVC
from sklearn.datasets import make_moons, make_circles, make_classification

# 接着我们生成一些随机数据来让我们后面去分类，为了数据难一点，我们加入了一些噪音。生成数据的同时把数据归一化
X, y = make_circles(noise=0.2, factor=0.5, random_state=1)
from sklearn.preprocessing import StandardScaler
X = StandardScaler().fit_transform(X)

# 我们先看看我的数据是什么样子的，这里做一次可视化如下：
from matplotlib.colors import ListedColormap
cm = plt.cm.RdBu
cm_bright = ListedColormap(['#FF0000', '#0000FF'])
ax = plt.subplot()

ax.set_title("Input data")
# Plot the training points
ax.scatter(X[:, 0], X[:, 1], c=y, cmap=cm_bright)
ax.set_xticks(())
ax.set_yticks(())
plt.tight_layout()
plt.show()
# 分类时我们使用了网格搜索，在C=(0.1,1,10)和gamma=(1, 0.1, 0.01)形成的9种情况中选择最好的超参数，
# 我们用了4折交叉验证。这里只是一个例子，实际运用中，你可能需要更多的参数组合来进行调参。
from sklearn.model_selection import GridSearchCV
grid = GridSearchCV(SVC(), param_grid={"C":[0.1, 1, 10], "gamma": [1, 0.1, 0.01]}, cv=4)
grid.fit(X, y)
print("The best parameters are %s with a score of %0.2f" % (grid.best_params_, grid.best_score_))

# 输出结果是The best parameters are {'C': 10, 'gamma': 0.1} with a score of 0.91
# 说明最好的参数是c=10，g=0.1

# 下面是普通的SVM分类后的可视化，对于这九种参数的可视化
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max,0.02),
                     np.arange(y_min, y_max, 0.02))

for i, C in enumerate((0.1, 1, 10)):
    for j, gamma in enumerate((1, 0.1, 0.01)):
        plt.subplot()
        clf = SVC(C=C, gamma=gamma)
        clf.fit(X,y)
        Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

        # Put the result into a color plot
        Z = Z.reshape(xx.shape)
        plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)

        # Plot also the training points
        plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm)

        plt.xlim(xx.min(), xx.max())
        plt.ylim(yy.min(), yy.max())
        plt.xticks(())
        plt.yticks(())
        plt.xlabel(" gamma=" + str(gamma) + " C=" + str(C))
        plt.show()