import sys

import numpy as np

'''
习得： 
    1、矩阵比对字符串
    2、创建矩阵数组-----None

n = np.arange(0, 30, 2)# start 0 step 2, stop before 30
n = n.reshape(3, 5) # reshape array to be 3x5
算方思想，利用伪矩阵比对两个字符串
'''
def getmaxStr(str1,str2):
    len1=len(str1)
    len2=len(str2)
    sb=''
    maxs=0  #最长公共字串的长度
    maxI=0    #记录公共字串最后一个符号的位置
    M=np.zeros((len1+1,len2+1))
    i=0
    while i<len1+1:
        M[i][0]=0
        i+=1
    j=0
    while j<len2+1:
        M[j][0]=0
        j+=1
    #利用递归公式填写矩阵
    i=1
    while i<len1+1:
        j=1
        while j<len2+1:
            if(list(str1)[i-1]==list(str2)[j-1]):
                M[i][j]=M[i-1][j-1]+1
                if(M[i][j]>maxs):
                    maxs=M[i][j]
                    maxI=i
            else:
                M[i][j]=0
            j+=1
        i+=1
    # print(M)
    #找出公共字串
    print(maxs)
    print(maxI)
    i=int(maxI-maxs)
    print(i)
    while i<maxI:
        sb+=str(str1[i])
        # print(list(str1)[i])
        i+=1
    return sb


'''
改进
    上个方法时间复杂度（m*n）空间复杂度（M*N）
改进后
    时间复杂度（（m+n）*n）空间复杂度（1）
'''
def getMaxStr(str1,str2):
    len1=len(str1)
    len2=len(str2)
    sb=''
    maxlen=0
    tempMaxlen=0
    maxLenEnd=0
    i=0
    while i<len1+len2:
        s1_begin=s2_begin=0
        tempMaxlen=0
        if i<len1:
            s1_begin=len1-i
        else:
            s2_begin=i-len1
        j=0
        print(str(i)+'-------------------------------------------------------------')
        while (s1_begin+j<len1)and (s2_begin+j<len2):
            print('s1_begin+j:'+str(s1_begin+j)+'   s2_begin+j:'+str(s2_begin+j)+'   j:'+str(j))
            print(list(str1)[s1_begin+j]+'***'+list(str2)[s2_begin+j])
            if(list(str1)[s1_begin+j]==list(str2)[s2_begin+j]):
                tempMaxlen+=1
            else:
                if (tempMaxlen>maxlen):
                    maxlen=tempMaxlen
                    maxLenEnd=s1_begin+j
                else:
                    tempMaxlen=0
            j+=1
        if tempMaxlen>maxlen:
            maxlen=tempMaxlen
            maxLenEnd=s1_begin+j
        i+=1
    i=maxLenEnd-maxlen
    while i<maxLenEnd:
        sb+=list(str1)[i]
        i+=1
    return  sb
print(getMaxStr('asde','deo'))
