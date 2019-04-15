import csv
import os
import re

import jieba
import numpy as np


def readCSV(filename):
    list=[]
    csv_file=csv.reader(open(filename,'r'))
    # print(csv_file)
    for each in csv_file:
        temp=[]
        temp.append(each[2].strip(']').strip('[').strip('\''))
        # print(each[2])
        temp.append(each[3].strip(']').strip('[').strip('\''))
        # print(each[3])
        # print(temp)
        list.append(temp)
    print('读取完毕！')
    return list
# readCSV('huaChina.csv')

def writeCSV(filename,list):
    # 打开文件，追加a
    out = open(filename, 'a', newline='')
    # 设定写入模式
    # csv_write = csv.writer(out, dialect='excel')  # 也可以是excel
    csv_write = csv.writer(out)#默认是csv
    # 写入具体内容
    for each in list:
        csv_write.writerow(each)
    print("write over")
# writeCSV('tet.csv',[])

def getStopWord(filename):
    stopwords = [line.strip() for line in open(filename, 'r', encoding='utf-8').readlines()]
    return stopwords
# list=[]
#     fil=open(filename,'r',encoding='utr-8')
#     for each in fil:
#         list.append(each.strip())
#     return list
def jieBaas(strings,stopWordList):
    strsList=[]
    fenci = jieba.cut(strings)  # 切分  句子
    for each in fenci:
        if each.strip() in  stopWordList:
            pass
        else:
            strsList.append(each)
    # print(strsList)
    return  strsList


def jieBaSplitWord(list):
    stopWord=getStopWord('StopWord.txt')    #加载停用词
    # jieba.load_userdict('yes.txt')          #加载自定义词典

    re_list=[]
    for i in range(1,len(list)):
        # print(list[i])
        temp=[]
        temp.append(list[i][0])
        # print(list[i][0])
        temp.append(jieBaas(list[i][1],stopWord))
        # print(temp)
        re_list.append(temp)
    return re_list

def loadData(filename):
    re_list=[]
    if not os._exists('temp.csv'):
        list=readCSV(filename)
        #分词，去停用词，写入
        re_list=jieBaSplitWord(list)
        writeCSV('temp.csv',re_list)
    else:
        re_list=readCSV('temp.csv')
    #     re_list=[['123',[1,2,3,4]],['123',[1,2,3,4],['123',[1,2,3,4],[]]
    return np.array(re_list)[:,1]

#
# list=loadData('huaChina.csv')
# for each in list:
#     print('=========================================================')
#     print(each)
# list=readCSV('huaChina.csv')
# # for each in list:
# #     print(each)