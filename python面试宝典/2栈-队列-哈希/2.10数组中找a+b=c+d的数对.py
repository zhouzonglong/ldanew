import  sys
'''
初级想法：数组分为大小两部分
          大小各取出两个进行判断

答案方法：字典法，键为和，值为数对
'''
class pair:
    def __init__(self,one,two):
        self.first=one
        self.second=two
def findPair(arr):
    sumPair=dict()
    n=len(arr)
    i=0
    while i<n:
        j=i+1
        while j<n:
            sum=arr[i]+arr[j]
            if sum not in sumPair:
                temp=pair(arr[i],arr[j])
                sumPair[sum]=temp
            else:
                temps=sumPair[sum]
                print(str(temps.first)+str(temps.second)+str(arr[i])+str(arr[j]))
                return True
            j+=1
        i+=1
    return False

temp=[1,2,3,4,5,6,7,8]
print(findPair(temp))