# 数组循环移动n
'''
自己的想法：定义一个temp，然后都和temp交换
交换n次，时间复杂度O(n)，空间复杂度O(1)
'''
def change(arr,n):
    lens=len(arr)
    j = n
    temp = arr[j % lens]
    for i in range(lens):
        temp,arr[(j+n)%lens]=arr[(j+n)%lens],temp
        j=(j+n)%lens
    return arr
# arr=[1,2,3,4,5,6,7]
# print(change(arr,3))

'''
翻转法
'''
def reverses(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
def shifts(arr,k):
    lens=len(arr)
    if arr==None:
        print('bad')
    else:
        k=k%lens
        reverses(arr,0,lens-1)
        reverses(arr, k, lens - 1)
        reverses(arr, 0, k-1)
    print(arr)
arr=[1,2,3,4,5,6,7]
print(arr)
shifts(arr,3)