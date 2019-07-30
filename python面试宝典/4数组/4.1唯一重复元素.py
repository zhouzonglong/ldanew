import  sys
'''
方法一：使用额外数组
'''
# list=[1,3,4,5,3]
# list2=[]
# dictionarys={}
# i=0
# for each in list:
#     if  each not in list2:
#         list2.append(each)
#     else:
#         # print(each)
#         pass
# '''
# 方法二：求和
# '''
# list=[1,2,3,4,3,5]
# a=0
# b=0
# for each in range(5):
#     a+=each
# for each in list:
#     b+=each
# b-a
# '''
# 方法三：使用异或
# '''
# def finddup(arry):
#     lens=len(arry)
#     result=0
#     i=0
#     while i<lens:
#         result^=arry[i]
#         i+=1
#     j=1
#     while j<lens:
#         result^=j
#         j+=1
#     return  result
# finddup([1,2,3,4,5,3])
'''
方法四：数据映射
        每读取一个数，把它变成他的相反数，判断是否已经存在这个数的相反数
        1,2,3,4,3
        -1，-2，-3，-4，-3重复
'''

'''
环形相遇法
'''

'''
问题：
【1,2,3.3.3.4.5.5.5.6】
找出重复的数字
'''
def findussp(arry,num):
    s=set()
    if None==arry:
        return  s
    lens=len(arry)
    index=arry[0]
    num=num-1
    while True:
        # print('\n\n***************'+str(index)+'***********')
        # print('***************'+str(arry[index])+'***********')
        if arry[index]<0:
            num-=1
            arry[index]=lens-num
            s.add(index)
            # print(index)
        if num==0:
            return  s
        arry[index]*=-1
        # print('array:'+str(arry[index]))
        index=arry[index]*(-1)
        # print('index:'+str(index))

array=[1,2,3,3,3,4,5,5,5,5,6]
num=6
s=findussp(array,num)
# for each in s:
#     print(each)

