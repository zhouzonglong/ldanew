ss='fdsj的kj个fk就ldsjl'
def getSize(c):
    return 3 if c>=u'\u4e00' and c<=u'\u9fa5' else 1
def getStr(strs,n):
    temp=0
    tempstr=''
    for i in range(len(strs)):
        if temp<n:
            temp+=getSize(strs[i])
            if temp<=n:
                tempstr+=strs[i]
        else:
            break
    print(tempstr)
getStr(ss,7)