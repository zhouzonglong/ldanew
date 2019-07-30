from sklearn.feature_extraction.text import TfidfVectorizer
tfidf2 = TfidfVectorizer()
corpus=["I come to China to travel",
    "This is a car polupar in China",
    "I love tea and Apple ",
    "The work is to write some papers in science"]
re = tfidf2.fit_transform(corpus)
print (re)
# 输出：
# 0, 4)	0.442462137895
#   (0, 15)	0.697684463384
#   (0, 3)	0.348842231692
#   (0, 16)	0.442462137895
#   (1, 3)	0.357455043342
#   (1, 14)	0.453386397373
#   (1, 6)	0.357455043342
#   (1, 2)	0.453386397373
#   (1, 9)	0.453386397373
#   (1, 5)	0.357455043342
#   (2, 7)	0.5
#   (2, 12)	0.5..................