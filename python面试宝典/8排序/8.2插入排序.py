import sys
'''
时间复杂度（n--n2）
空间复杂度（1）
'''
def insert_sort(lists):
    count=len(lists)
    for i in range(1,count):
        # print(str(i)+'---------------------')
        key=lists[i]
        j=i-1
        while j>=0:
            # print(j)
            if lists[j]>key:
                lists[j+1]=lists[j]
                lists[j]=key
            j-=1
        print(lists)
    return lists
list=[2,4,3,1,7,0,5,9]
print('原始数据：')
# print(list)
print(insert_sort(list))
