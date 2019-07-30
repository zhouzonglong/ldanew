'''
题目：一个数组有三个数出现一次，其他都是出现欧次找出一个
利用bit划分数组，一半为奇数一半为偶数，同时每组数异或
'''
def isOne(n,i):
    return (n&(1<<i))==1
def findSingle(arr):
    size=len(arr)
    i=0
    while i<32:
        result1=result0=count1=count0=0
        j=0
        while j<size:
            if isOne(arr[j],i):
                result1^=arr[j]
                count1+=1
            else:
                result0^=arr[j]
                count0+=1
            j+=1
        i+=1
        if count1%2==1 and result0!=0:
            return  result1
        if count0%2==1 and result1!=0:
            return result0
    return -1
print(findSingle([6,3,4,5,9,4,3]))
# n=findSingle([9,4,5,6,6,5,4,3,7])
# if n!=-1:
#     print(n)
# else:
#     print('no')