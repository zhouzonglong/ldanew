# import modules & set up logging
# 在gensim中，word2vec 相关的API都在包gensim.models.word2vec中。和算法有关的参数都在类gensim.models.word2vec.Word2Vec中。算法需要注意的参数有：
#
# 　　　　1) sentences: 我们要分析的语料，可以是一个列表，或者从文件中遍历读出。后面我们会有从文件读出的例子。
#
# 　　　　2) size: 词向量的维度，默认值是100。这个维度的取值一般与我们的语料的大小相关，如果是不大的语料，比如小于100M的文本语料，则使用默认值一般就可以了。如果是超大的语料，建议增大维度。
#
# 　　　　3) window：即词向量上下文最大距离，这个参数在我们的算法原理篇中标记为c，window越大，则和某一词较远的词也会产生上下文关系。默认值为5。在实际使用中，可以根据实际的需求来动态调整这个window的大小。如果是小语料则这个值可以设的更小。对于一般的语料这个值推荐在[5,10]之间。
#
# 　　　　4) sg: 即我们的word2vec两个模型的选择了。如果是0， 则是CBOW模型，是1则是Skip-Gram模型，默认是0即CBOW模型。
#
# 　　　　5) hs: 即我们的word2vec两个解法的选择了，如果是0， 则是Negative Sampling，是1的话并且负采样个数negative大于0， 则是Hierarchical Softmax。默认是0即Negative Sampling。
#
# 　　　　6) negative:即使用Negative Sampling时负采样的个数，默认是5。推荐在[3,10]之间。这个参数在我们的算法原理篇中标记为neg。
#
# 　　　　7) cbow_mean: 仅用于CBOW在做投影的时候，为0，则算法中的xw为上下文的词向量之和，为1则为上下文的词向量的平均值。在我们的原理篇中，是按照词向量的平均值来描述的。个人比较喜欢用平均值来表示xw,默认值也是1,不推荐修改默认值。
#
# 　　　　8) min_count:需要计算词向量的最小词频。这个值可以去掉一些很生僻的低频词，默认是5。如果是小语料，可以调低这个值。
#
# 　　　　9) iter: 随机梯度下降法中迭代的最大次数，默认是5。对于大语料，可以增大这个值。
#
# 　　　　10) alpha: 在随机梯度下降法中迭代的初始步长。算法原理篇中标记为η，默认是0.025。
#
# 　　　　11) min_alpha: 由于算法支持在迭代的过程中逐渐减小步长，min_alpha给出了最小的迭代步长值。随机梯度下降中每轮的迭代步长可以由iter，alpha， min_alpha一起得出。这部分由于不是word2vec算法的核心内容，因此在原理篇我们没有提到。对于大语料，需要对alpha, min_alpha,iter一起调参，来选择合适的三个值。
import logging
import os
from gensim.models import word2vec

#-------------------------------------------------模型训练
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences = word2vec.LineSentence('./in_the_name_of_people_segment.txt')
model = word2vec.Word2Vec(sentences, hs=1,min_count=1,window=3,size=100)

#模型使用
#----------------------------------------------1、找出最近的词集合-----------------------------------------
req_count = 5
for key in model.wv.similar_by_word('沙瑞金'.decode('utf-8'), topn =100):
    if len(key[0])==3:
        req_count -= 1
        print (key[0], key[1])
        if req_count == 0:
            break
# 输出
# 高育良 0.967257142067
# 李达康 0.959131598473
# 田国富 0.953414440155
# 易学习 0.943500876427
# 祁同伟 0.942932963371


#-------------------------------------------2、第二个应用是看两个词向量的相近程度，这里给出了书中两组人的相似程度：----------------------------------

print (model.wv.similarity('沙瑞金'.decode('utf-8'), '高育良'.decode('utf-8')))
print (model.wv.similarity('李达康'.decode('utf-8'), '王大路'.decode('utf-8')))
# 0.961137455325
# 0.935589365706


# -----------------------------------------------3、第三个应用是找出不同类的词，这里给出了人物分类题：-----------------------------------------------
print (model.wv.doesnt_match(u"沙瑞金 高育良 李达康 刘庆祝".split()))
# word2vec也完成的很好，输出为"刘庆祝"。
