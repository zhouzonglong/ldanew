import sys
'''
输入：str1='hfgjdshjdkshs'
      x='hfgjd'
输出  return shjdkshs
'''
# def haves(strLong,strsShort):
#     j=0
#     if strLong=="":
#         return None
#     for i in range(len(strsShort)):
#         if list(strsShort)[i]==list(strLong)[j]:
#             i+=1
#             j+=1
#         if i!=j:
#             return None
#     if j==len(strsShort):
#         return strLong[j:]
def haves(strLong,strsShort):
    if strLong=="":
        return None
    lensShort=len(strsShort)
    temp=''.join(list(strLong)[0:lensShort])
    if temp==strsShort:
        return strLong[lensShort:]
    return None
# ['testbattingcat', 'testingtest', 'testertest','testing', 'batting', 'tester', 'apple', 'test', 'bat','cat']
def fun(strs,arr):
    tempStrs=strs
    while strs!=None:
        if strs!=None and len(strs)==0:
            return True
        for each in arr:
            tempStrs=haves(strs, each)
            if tempStrs==None:
                continue
            else:
                arr.remove(each)
                # tempStrs = haves(tempStrs, arr)
                break
        strs=tempStrs
    return False
# def baseIfhave(strs,arr):
#     tempList=[]
#     print('--------------------------------')
#     print(strs)
#     print(arr)
#     for each in arr:
#         # print(each)
#
#         if list(each)[0]==list(strs)[0]:
#             x=haves(strs,each)
#             if x!=None:
#                 tempList.append(each)
#                 strs=x
#                 arr.remove(each)
#                 strs=baseIfhave(strs,arr)
#     return strs
def main(arr):
    # 此处可以优化，小于最后两个串长和的不参与for
    for i in range(len(arr)-1):
        # print('=======================================%d======================================'%i)
        bools=fun(arr[i],arr[i+1:])
        if bools==True:
            print(arr[i])
        else:
            # print('no')
            pass

arr=['testbattingcat', 'testingtest', 'testertest','testing', 'batting', 'tester', 'apple', 'test', 'bat','cat']
main(arr)
