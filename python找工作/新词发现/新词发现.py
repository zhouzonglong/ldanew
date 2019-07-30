import numpy as np

def calc_ent(x):

    x_value_list = set([x[i] for i in range(x.shape[0])])
    ent = 0.0
    for x_value in x_value_list:
        p = float(x[x == x_value].shape[0]) / x.shape[0]
        log_p = np.log2(p)
        ent -= p * log_p

    return ent

import re
# import pymongo
from tqdm import tqdm
import hashlib
from collections import defaultdict

'''
读取文本，返回分段好的串
'''
def getTxts():
    with open('text.txt',encoding='utf-8') as file:
        texts=file.read()
        for t in re.split(u'[^\u4e00-\u9fa50-9a-zA-Z]+', texts):    #删除各个字符保留文字、英文
            if t:
                yield t

# db = pymongo.MongoClient().weixin.text_articles
# md5 = lambda s: hashlib.md5(s).hexdigest()
# def texts():
#     texts_set = set()
#     for a in tqdm(db.find(no_cursor_timeout=True).limit(3000000)):
#         if md5(a['text'].encode('utf-8')) in texts_set:
#             continue
#         texts_set.add(md5(a['text'].encode('utf-8')))
#         for t in re.split(u'[^\u4e00-\u9fa50-9a-zA-Z]+', a['text']):
#             if t:
#                 yield t
#     print (u'最终计算了%s篇文章'%len(texts_set))
'''
统计词频以及总词数
'''
n = 4
min_count = 2
def getStrsNumDic():
    ngrams = defaultdict(int)
    for t in getTxts():
        for i in range(len(t)):
            for j in range(1, n+1):
                if i+j <= len(t):
                    # print(t[i:i+j])
                    ngrams[t[i:i+j]] += 1
    ngrams = {key:numbers for key,numbers in ngrams.items() if numbers >= min_count}
    total = 1.*sum([numbers for key,numbers in ngrams.items() if len(key) == 1])
    return  ngrams,total
print('0000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
ngrams, total=getStrsNumDic()
def is_keep(s, min_proba):
    if len(s) >= 2:
        # print(s)
        # print(s[1:])
        tempList=[total*ngrams[s]/(ngrams[s[:key+1]]*ngrams[s[key+1:]]) for key in range(len(s)-1)]
        # print(tempList)
        # print('------------------------------')
        score = min(tempList)
        if score > min_proba[len(s)]:
            return True
    else:
        return False

min_proba = {2:10, 3:25, 4:125}
# print(ngrams)
# print(len(ngrams))
ngrams_ = set(key for key,numbers in ngrams.items() if is_keep(key, min_proba))
# print(ngrams_)
# print(len(ngrams_))


def cut(s):
    # print('-----------------------------------')
    # print(ngrams)
    r = np.array([0]*(len(s)-1))
    # print(s)
    # print(r)
    for i in range(len(s)-1):
        for j in range(2, n+1):
            temp=s[i:i+j]
            # print('jkfdjkfjdk--'+str(temp))
            if temp in ngrams_:
                # print('=====' + str(temp))
                r[i:i + j - 1] += 1
    w = [s[0]]
    for i in range(1,len(s)):
        if r[i-1] > 0:
            w[-1] += s[i]
        else:
            w.append(s[i])
    # print(w)
    # print(r)
    return w

words = defaultdict(int)
for t in getTxts():
    for i in cut(t):
        words[i] += 1
        # print(words)
words = {i:j for i,j in words.items() if j >= min_count}
# print(words)


def is_real(s):
    if len(s) >= 3:
        for i in range(3, n+1):
            for j in range(len(s)-i+1):
                if s[j:j+i] not in ngrams_:
                    return False
        return True
    else:
        return True
print('=========================================================================================================')
print(words)
w = {i:j for i,j in words.items() if is_real(i)  and len(i)>1}

print(w)
# print(len(w))
# print(ngrams_)
# print(len(ngrams_))





