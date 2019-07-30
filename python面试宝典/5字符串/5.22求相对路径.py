path1=r'rr/r/a/b/c/d/ddf.txt'
path2=r'rr/r/eg/gg/g.tdt'
def getRelativePath(path1,path2):
    print(path1)
    print(path2)
    list1=path1.split('/')
    list2 = path2.split('/')

    lens1=len(list1)
    lens2=len(list2)
    j=0
    for i in range(min(lens1,lens2)):
        if list1[i]==list2[i]:
            list1[i]=''
            list2[i]=''
            j+=1
    list1=list1[j:]
    list2 = list2[j:]
    paths=''
    for i in range(len(list1)-1):
        paths+='../'
    paths+='/'.join(list2)
    return paths
print(getRelativePath(path1,path2))