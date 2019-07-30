import sys

'''
难点：中文的编码不是utf8，而是unicode

数据获取：通用的爬虫我一般使用beautifulsoup。但是我们我们需要某些特殊的语料数据，比如上面提到的“机器学习”相关的语料库，则需要用主题爬虫（也叫聚焦爬虫）来完成。这个我一般使用ache。 ache允许我们用关键字或者一个分类算法来过滤出我们需要的主题语料，比较强大。
'''
#从文件导入--------------------------------------------------------停用词表--------------------------------------------
stpwrdpath = "stop_words.txt"
stpwrd_dic = open(stpwrdpath, 'rb')
stpwrd_content = stpwrd_dic.read()
#将停用词表转换为list
stpwrdlst = stpwrd_content.splitlines()
stpwrd_dic.close()
# 向量化
# ---------------------------------------------------------------------读取训练文本---------------------------------------------
with open('./nlp_test1.txt') as f3:
    res1 = f3.read()
print (res1)
with open('./nlp_test3.txt') as f4:
    res2 = f4.read()
print (res2)

# -------------------------------------------------------------------向量化、TF-IDF、标准化------------------------------------------------------------
# 现在我们可以进行向量化、TF-IDF、标准化三步处理了。注意，这里我们引入了我们上面的停用词表。

from sklearn.feature_extraction.text import TfidfVectorizer
corpus = [res1,res2]
vector = TfidfVectorizer(stop_words=stpwrdlst)
tfidf = vector.fit_transform(corpus)
print (tfidf)

# ----------------------------------------------------------------------测试输出-----------------------------------------------------------
wordlist = vector.get_feature_names()#获取词袋模型中的所有词
# tf-idf矩阵 元素a[i][j]表示j词在i类文本中的tf-idf权重
weightlist = tfidf.toarray()
#打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
for i in range(len(weightlist)):
    print ("-------第",i,"段文本的词语tf-idf权重------"  )
    for j in range(len(wordlist)):
        print (wordlist[j],weightlist[i][j] )

# 部分输出如下：
#
# -------第 0 段文本的词语tf-idf权重------
# 一起 0.217098590137
# 万块 0.217098590137
# 三人 0.217098590137
# 三套 0.0
# 下海经商 0.217098590137
# .....
# -------第 1 段文本的词语tf-idf权重------
# .....
# 李达康 0.0995336411066
# 欧阳 0.279782119316
# 毛娅 0.419673178975
# 沙瑞金 0.0995336411066
# 没想到 0.0
# 没有 0.139891059658
# 浪费 0.139891059658
# 王大路 0.29860092332
# .....





