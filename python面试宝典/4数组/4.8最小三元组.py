'''
蛮力法不推荐（时间O(l*m*n)）
三个数组，求min（max（|a-b|，|b-c|，|a-c|））
每次遍历最小数字所在的数组
'''
def mins(a,b,c):
    min=a
    if min>b:
        min=b
    if min>c:
        min=c
    return min
def maxs(a,b,c):
    max=abs(a-b)
    if max<abs(a-c):
        max=abs(a-c)
    if max<abs(b-c):
        max=abs(b-c)
    return max
def getMinDistance(A,B,C):
    distances=2**32
    tempDis=0
    lenA=len(A)
    lenB=len(B)
    lenC=len(C)
    i=0
    j=0
    k=0
    while True:
        tempDis=maxs(A[i],B[j],C[k])

        if tempDis<distances:
            distances=tempDis
        tempnum = min(A[i], B[j], C[k])
        if tempnum==A[i]:
           i+=1
           if i>=lenA:
               break
        if tempnum==B[j]:
           j+=1
           if j>=lenB:
               break
        if tempnum==C[k]:
           k+=1
           if k>=lenC:
               break
    return distances
A=[3,4,5,7,15]
B=[10,12,14,16,17]
C=[20,21,23,24,30,37]
print(getMinDistance(A,B,C))




