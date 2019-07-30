import sys
'''
时间复杂度O(n2)
空间复杂度O(1)
'''
def select_sort(lists):
    count=len(lists)
    for i in range(0,count):
        # print(str(i)+'---------------------')
        min=i
        for j in range(i+1,count):
            if(lists[min]>lists[j]):
                min=j
        key=lists[min]
        lists[min]=lists[i]
        lists[i]=key

    return lists
list=[33,14,27,51,69]
print(select_sort(list))
