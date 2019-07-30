import math
import sys
'''基数排序'''
def radix_sort(lists,radix=10):
    # max_num=max(lists)
    # print(max_num)
    # log_max=math.log(max_num,radix)
    # print(log_max)
    # k=int(math.ceil(log_max))
    k=2  #位数
    bucket=[[] for i in range(radix)]
    for i in range(1,k+1):
        print('00000000000000000000000000000000000000000000000000000000')
        for j in lists:
            bucket[int(j/(radix**(i-1))%radix**i)].append(j)
            # print(str(j)+'--'+str(j/(radix**(i-1))%radix**i)+'--'+str(j/(radix**(i-1))))
            print(bucket)
        print('------------------------------')
        del lists[:]
        for z in bucket:
            lists+=z
            print(lists)
            del z[:]
    return lists
list=[13,36,38,24,91,77,45]
list=radix_sort(list)
print(list)
