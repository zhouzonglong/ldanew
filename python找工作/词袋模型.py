from sklearn.feature_extraction.text import CountVectorizer
vectorizer=CountVectorizer()
corpus=["I come to China to travel",
    "This is a car polupar in China",
    "I love tea and Apple ",
    "The work is to write some papers in science"]
print (vectorizer.fit_transform(corpus))
# 输出
# (0, 16)	1
#   (0, 3)	1
#   (0, 15)	2
#   (0, 4)	1
#   (1, 5)	1
#   (1, 9)	1
#   (1, 2)	1
#   (1, 6)	1
#   (1, 14)	1
#   (1, 3)	1
#   (2, 1)	1
#   (2, 0)	1
#   (2, 12)	1
#   (2, 7)	1
#   (3, 10)	1
#   (3, 8)	1
#   (3, 11)	1
#   (3, 18)	1
#   (3, 17)	1
#   (3, 13)	1
#   (3, 5)	1
#   (3, 6)	1
#   (3, 15)	1
print (vectorizer.fit_transform(corpus).toarray())
print (vectorizer.get_feature_names())
# 输出
# [[0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 2 1 0 0]
#  [0 0 1 1 0 1 1 0 0 1 0 0 0 0 1 0 0 0 0]
#  [1 1 0 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0 0]
#  [0 0 0 0 0 1 1 0 1 0 1 1 0 1 0 1 0 1 1]]
# ['and', 'apple', 'car', 'china', 'come', 'in', 'is', 'love', 'papers', 'polupar', 'science', 'some', 'tea', 'the', 'this', 'to', 'travel', 'work', 'write']

'''
特征降维
'''
from sklearn.feature_extraction.text import HashingVectorizer
vectorizer2=HashingVectorizer(n_features = 6,norm = None)
print (vectorizer2.fit_transform(corpus))
# 输出
# 　可以看出4个文本的词频已经统计出，在输出中，左边的括号中的第一个数字是文本的序号
# ，第2个数字是词的序号，注意词的序号是基于所有的文档的。第三个数字就是我们的词频。
# #  (0, 1)	2.0
#   (0, 2)	-1.0
#   (0, 4)	1.0
#   (0, 5)	-1.0
#   (1, 0)	1.0
#   (1, 1)	1.0
#   (1, 2)	-1.0
#   (1, 5)	-1.0
#   (2, 0)	2.0
#   (2, 5)	-2.0
#   (3, 0)	0.0
#   (3, 1)	4.0
#   (3, 2)	-1.0
#   (3, 3)	1.0
#   (3, 5)	-1.0




