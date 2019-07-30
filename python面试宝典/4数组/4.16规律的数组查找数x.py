import numpy as np


def findX(arr,x):
    m,n=np.array(arr).shape
    m-=1
    n-=1
    j=0
    if x<arr[0][0] or x>arr[m][n]:
        return False
    else:
        while n>=0 and j<=m:
            if arr[j][n]==x:
                return True
            elif x>arr[j][n]:
                j+=1
            else:
                n-=1
    return False
arr=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(np.array(arr))
print(findX(arr,1))
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]
#  [13 14 15 16]]