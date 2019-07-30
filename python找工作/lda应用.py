import jieba
# LDA特征提取流程：
# 1、文档读取--分词--存储
# 2、文档读取--去停用词-
# 3、向量化
# 4、LDA训练
# 5、主题和文档分布、文档和词分布
# 6、聚类、分类

# =======================================================--1、文档读取--分词--存储--==========================================================================
jieba.suggest_freq('沙瑞金', True)
jieba.suggest_freq('易学习', True)
# 第一个文档分词#
with open('./nlp_test0.txt') as f:
    document = f.read()

    document_decode = document.decode('GBK')
    document_cut = jieba.cut(document_decode)
    # print  ' '.join(jieba_cut)
    result = ' '.join(document_cut)
    result = result.encode('utf-8')
    with open('./nlp_test1.txt', 'w') as f2:
        f2.write(result)
f.close()
f2.close()
# =======================================================--2、文档读取--去停用词--==========================================================================
with open('./nlp_test1.txt') as f3:
    res1 = f3.read()
with open('./nlp_test3.txt') as f4:
    res2 = f4.read()
with open('./nlp_test5.txt') as f5:
    res3 = f5.read()

#从文件导入停用词表
stpwrdpath = "stop_words.txt"
stpwrd_dic = open(stpwrdpath, 'rb')
stpwrd_content = stpwrd_dic.read()
#将停用词表转换为list
stpwrdlst = stpwrd_content.splitlines()
stpwrd_dic.close()
#  =======================================================--3、向量化--==========================================================================
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
corpus = [res1,res2,res3]
cntVector = CountVectorizer(stop_words=stpwrdlst)
cntTf = cntVector.fit_transform(corpus)
# =======================================================--4、LDA训练--==========================================================================
lda = LatentDirichletAllocation(n_topics=2,
                                learning_offset=50.,
                                random_state=0)
docres = lda.fit_transform(cntTf)
# =======================================================--5、主题和文档分布、文档和词分布--==========================================================================
print (docres)
print (lda.components_)
# =======================================================--6、聚类、分类--==========================================================================
