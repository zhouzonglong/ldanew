import sys
from datetime import datetime
from time import time

'''
问题：数组中找到最短路径，从oo---nm
方法一：递归          f（i+1）=f(i)+c

      从最后节点出发
'''
def getMiniPath(arr,i,j):
    if i==0 and j==0:
        return arr[i][j]
    elif i>0 and j>0:
        return arr[i][j]+min(getMiniPath(arr,i-1,j),getMiniPath(arr,i,j-1))
    elif i>0 and j==0:
        return arr[i][j]+getMiniPath(arr,i-1,j)
    else:
        return arr[i][j]+getMiniPath(arr,i,j-1)
arr=[[1,4,3],[8,7,5],[2,1,5]]
tim1=datetime.now()
print(tim1.second)
getMiniPath(arr,2,2)
tim2=datetime.now()
print(tim2.second)

'''
方法二：动态规划

从第一个节点求，以便能够利用前面的节点值
'''
def getMiniPath2(arr,row,col):
    cache=[[None]*col]*row
    cache[0][0]=arr[0][0]
    i=1
    while i<col:
        cache[0][i]=cache[0][i-1]+arr[0][i]
        i+=1
    j=1
    while j<row:
        cache[j][0]=cache[j-1][0]+arr[j][0]
        j+=1
    #建立一个cache与原数组同等大小
    print('路径：')
    i=1
    while i<row:
        j=1
        while j<row:
            if cache[i-1][j]>cache[i][j-1]:
                cache[i][j]=arr[i][j]+cache[i][j-1]
                print(str(i)+'======'+str(j-1))
            else:
                cache[i][j] = arr[i][j] + cache[i-1][j]
                print(str(i-1) + '======' + str(j))
            j+=1
        i+=1
    print(str(row) + '======' + str(col))

tim1=time()
print(tim1)
getMiniPath2(arr,2,2)
tim2=time()
print(tim2)