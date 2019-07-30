import sys

'''
for i in range(0,int((size/2)))[::-1]:
后面【：：-1】那么i从最后一个数开始
'''
def adjuct_heap(lists,i,size):
    lchild=2*i+1
    rchild=2*i+2
    maxs=i
    if i<size/2:
        if lchild<size and lists[lchild]>lists[maxs]:
            maxs=lchild
        if rchild<size and lists[rchild]>lists[maxs]:
            maxs=rchild
        if maxs!=i:
            lists[maxs],lists[i]=lists[i],lists[maxs]
            adjuct_heap(lists,maxs,size)

def buile_heap(lists,size):
    for i in range(0,int((size/2)))[::-1]:
        adjuct_heap(lists,i,size)
        print(lists)

def heap_sort(lists):
    size=len(lists)
    buile_heap(lists,size)
    print('--------------------------------')
    for i in range(0,(size))[::-1]:
        lists[0],lists[i]=lists[i],lists[0]
        adjuct_heap(lists,0,i)
        print(lists)

list=[1,2,3,4,5,6,7,8]
print('原始数据：')
print(list)
heap_sort(list)
# print(list)
