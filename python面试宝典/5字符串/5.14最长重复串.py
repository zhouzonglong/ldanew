def getMaxDupChar(s,startIndex,maxs,temp):
    if startIndex==len(s)-1:
        return  max(maxs,temp)
    if list(s)[startIndex]==list(s)[startIndex+1]:
        return getMaxDupChar(s,startIndex+1,maxs+1,temp)
    else:
        return getMaxDupChar(s,startIndex+1,1,max(maxs,temp))
print(getMaxDupChar('abbbvv',0,1,1))


# 5.15 最长子序列（递增）
def getMax(arr):
    maxlong=1
    temp=1
    for i in range(len(arr)-1):
        if arr[i]<arr[i+1]:
            temp+=1
        else:
            maxlong=max(temp,maxlong)
    return maxlong
print(getMax('xbcdza'))