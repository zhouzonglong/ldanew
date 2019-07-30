'''
方法一：两重循环
'''
def maxSubArry(arr):
    if arr==None or len(arr)<1:
        return
    maxSum=-2**31
    i=0
    while i<len(arr):
        sums=0
        j=i
        while j<len(arr):
            sums+=arr[j]
            if sums>maxSum:
                maxSum=sums
            j+=1
        i+=1
    return maxSum
arr=[1,-2,4,8,-4,7,-1,-9,-8,-5,10,-1]
# print(maxSubArry(arr))
'''
方法二：动态规划
'''
def maxSubArry2(arr):
    n=len(arr)
    End=[None]*n
    All=[None]*n
    End[n-1]=arr[n-1]
    All[n - 1] = arr[n - 1]
    End[0]=All[0]=arr[0]
    i=1
    while i<n:
        End[i]=max(End[i-1]+arr[i],arr[i])
        All[i]=max(End[i],All[i-1])
        print('arr' + str(arr))
        print('End'+str(End))
        print('All'+str(All))
        print('------------------------------------------')
        i+=1
    return All[n-1]
# print(maxSubArry2(arr))
'''
方法三：优化动态规划
'''
def maxSubArry3(arr):
    n=len(arr)
    End=All=arr[0]
    i=1
    while i<n:
        End=max(End+arr[i],arr[i])
        All=max(End,All)
        i+=1
    return All
print(maxSubArry3(arr))


'''
找出起始和终止位置
'''
