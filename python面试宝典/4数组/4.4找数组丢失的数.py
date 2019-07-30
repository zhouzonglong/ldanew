def getNum(list):
    # if list==None or len(list)<1:
    #     return  -1
    a=list[0]
    lens=len(list)
    b=1
    i=1
    while i<lens:
        a=a^list[i]
        i+=1
    i=2
    while i<=lens+1:
        b=b^i
        i+=1
    return  a^b
list=[1,4,3,2,7,5]
print(getNum(list))
