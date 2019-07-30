import datetime
import time


def compare(str1,str2,char_to_int):
    len1=len(str1)
    len2=len(str2)
    i=0
    j=0
    while i<len1 and j<len2:
        if list(str1)[i] not in char_to_int.keys():
            char_to_int[list(str1)[i]]=-1
        if list(str2)[i] not in char_to_int.keys():
            char_to_int[list(str2)[j]]=-1
        if char_to_int[list(str1)[i]]<char_to_int[list(str2)[j]]:
            return -1
        if char_to_int[list(str1)[i]]>char_to_int[list(str2)[j]]:
            return 1
        else:
            i+=1
            j+=1
        if i==len1 and j==len2:
            return 0
        elif i==len1:
            return -1
        else:
            return 1
def insertSort(s,char_to_int):
    lens=len(s)
    i=1
    while i<lens:
        temp=s[i]
        j=i-1
        while j>=0:
            if compare(temp,s[j],char_to_int)==-1:
                s[j+1]=s[j]
            else:
                break
            j-=1
        s[j+1]=temp
        i+=1
def test1():
    time1=time.clock()
        # datetime.datetime.now()
        # time.monotonic()
    s=["bed","dog","dear","eye","daa","fed","oog","gar","eeye","cdaa"]
    sequence='dgecfboa'
    lens=len(sequence)
    char_to_int=dict()
    i=0
    while i<lens:
        char_to_int[list(sequence)[i]]=i
        i+=1
    insertSort(s,char_to_int)
    time2= time.clock()
        # datetime.datetime.now()
    # i=0
    # while i<len(s):
    #     print(s[i])
    #     i+=1
    # print(time1)
    # print(time2)
    print("%.6f"%(time2-time1))
test1()
#======================================================
'''
比较两个字符串的大小
'''
def compard(sequence,str1,str2):
    lens1=len(str1)
    lens2=len(str2)
    i=0
    j=0
    while i<lens1 and j<lens2:
        try:
            tempi=sequence.index(list(str1)[i])
        except:
            return 8
        try:
            tempj=sequence.index(list(str2)[j])
        except:
            return -1

        if tempi<tempj:
            return  8
        elif tempi<tempj:
            return -1
        else:
            i+=1
            j+=1
    return -1
'''
sequence:所给的序列
s：串数组
'''
def mySort(sequence,s):
    #对s进行排序
    lens=len(s)
    for i in range(lens):
        for j in range(i+1,lens):
            if compard(sequence,s[i],s[j])==8:
                s[i],s[j]=s[j],s[i]
    return s


time1=time.clock()
s=["bed","dog","dear","eye","daa","fed","oog","gar","eeye","cdaa"]
sequence='dgecfboa'
s=mySort(sequence,s)
time2= time.clock()
    # datetime.datetime.now()
# i=0
# while i<len(s):
#     print(s[i])
#     i+=1
# print(time1)
# print(time2)
print("%.6f"%(time2-time1))

