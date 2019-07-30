#【2,2,4,5,6,4,3,6,4，5，4】 4,5最短距离
def minidistance(arr,num1,num2):
    mindis=2**32
    dist=0
    i=0
    while i<len(arr):
        if arr[i]==num1:
            j=0
            while arr[j]==num2:
                dist=abs(i-j)
                if dist<mindis:
                    mindis=dist
                j+=1
        i+=1
    return  mindis

# print(minidistance([4,5,7,6,54,6,87,9,6,6,4,5],6,4))

'''
方法二：动态规划
'''
def  getm(arr,num1,num2):
    lastPos1=-1
    lastPos2=-1
    mindis=2**32
    i=0
    while i<len(arr):
        if  arr[i]==num1:
            lastPos1=i
            print('lastpos11111:'+str(lastPos1))
            if  lastPos2>=0:
                mindis=min(mindis,lastPos1-lastPos2)
        if arr[i]==num2:
            lastPos2=i
            print('lastpos2222:'+str(lastPos2))
            if lastPos1>=0:
                mindis=min(mindis,lastPos2-lastPos1)
        i+=1
    return  mindis
print(getm([4,5,6,5,7,3,2,6,4,7],4,6))
