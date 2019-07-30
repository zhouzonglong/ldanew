def shell_sort(lists):
    count = len(lists)
    step=2
    group=count/step
    group_int=int(group)
    while group_int>0:
        lists=setorss(lists,group_int)
        group_int=int(group_int/step)
    return lists
def setorss(lists,group):
    for i in range(0,group):
        count=len(lists)
        j=i+group
        while j<count:
            k=j-group
            key=lists[j]
            while k>=0:
                if lists[k]>key:
                    lists[k+group]=lists[k]
                    lists[k]=key
                k-=group
            j+=group
        print(lists)
    return lists
list=[7,6,5,4,3,2,1,0]
print('原始数据：')
print(list)
print(shell_sort(list))