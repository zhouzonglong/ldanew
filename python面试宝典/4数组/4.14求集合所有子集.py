'''
位图法：申请同长度数组，每次加一，为一的则输出为零的不输出
'''
# def getAllSubse(array,mark,c):
#     length=len(array)
#     if length==c:
#         print('{',end="")
#         i=0
#         while i<length:
#             if mark[i]==1:
#                 print(array[i],end="")
#             i+=1
#         print('}')
#     else:
#         mark[c]=1
#         getAllSubse(array,mark,c+1)
#         mark[c]=0
#         getAllSubse(array,mark,c+1)
# arry=['a','b','c']
# mark=[0,0,0]
# # getAllSubse(arry,mark,0)


# '''
# 迭代法：即使有重复数字也没事
# '''
# def getAllSub(str):
#     if str==None or len(str)<1:
#         print('bad')
#         return None
#     arr=[]
#     arr.append(str[0:1])
#     i=1
#     while i<len(str):
#         lens=len(arr)
#         j=0
#         while j<lens:
#            arr.append(arr[j]+str[i])
#            j+=1
#         arr.append(str[i:i+1])
#         i+=1
#     return arr
# print(getAllSub("abc"))
def getlistAll(list,x):
    temp=[]
    if len(list)>0:
        for each in list:
            temp.append(each+x)
            temp.append(each)
    temp.append(x)
    return  temp
def getAllSubse2(array):
    lis=[]
    lis.append(array[0])
    for i in range(1,len(array)):
        lis=getlistAll(lis,array[i])
    print(lis)

try:
    # print(getlistAll((['a', 'b', 'c']),'p'))
    getAllSubse2(['a','c','d'])
except:
    print('no')