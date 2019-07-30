def merge(left,right):
    i,j=0,0
    result=[]
    while i<len(left)and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=left[i:]
    result+=right[j:]
    return result
def merge_sort(lists):
    if(len(lists)<=1):
        return lists
    else:
        num=int(len(lists)/2)
        print(num)
        left=merge_sort(lists[:num])
        right=merge_sort(lists[num:])
    return merge(left,right)

list=[3,6,8,2,9]
list=merge_sort(list)
print(list)
