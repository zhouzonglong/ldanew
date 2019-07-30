
def getNum(arr):
    result=0
    positon=0
    i=0
    while i<len(arr):
        result=result^arr[i]
        i+=1
    tempresult=result
    print(tempresult)
    i=result
    while i&1==0:
        positon+=1
        i=i>>1
    print(positon)
    i=1
    while i<len(arr):
        if ((arr[i]>>positon)&1)==1:
            result=result^arr[i]
        i+=1
    # print(result)
    # print(result^tempresult)
arr=[3,3,4,6,6,7,8,8]
getNum(arr)






