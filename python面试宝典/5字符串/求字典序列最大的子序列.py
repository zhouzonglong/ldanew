'''
逆序遍历
'''
def getLargestSub(src):
    if src==None:
        return None
    lens=len(src)
    largestSub=[None]*(lens+1)
    largestSub[0]=list(src)[lens-1]
    i=lens-2
    j=0
    while i>0:
        # if ord(list(src)[i])>=ord(largestSub[j]):
        if list(src)[i] >= largestSub[j]:
            j+=1
            largestSub[j]=list(src)[i]
        i-=1
    largestSub=largestSub[0:j+1]
    i=0
    while i<j:
        temp=largestSub[i]
        largestSub[i]=largestSub[j]
        largestSub[j]=temp
        i+=1
        j-=1
    return ''.join(largestSub)
s='acbdxmng'
print(getLargestSub(s))