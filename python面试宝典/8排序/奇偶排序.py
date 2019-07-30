import sys
'''
奇偶排序
'''
def sort(list):
    i=0
    length=len(list)
    for i in range(length):
        if i%2==0:
            for k in range(length-1):
            # 偶排序
                if k%2==0:
                    if list[k]>list[k+1]:
                        temp=list[k]
                        list[k]=list[k+1]
                        list[k+1]=temp
        else:
            # 奇排序
            for k in range(length-1):
                if k%2!=0:
                    if list[k]>list[k+1]:
                        temp=list[k]
                        list[k]=list[k+1]
                        list[k+1]=temp
    return list
list=[2,6,9,4,7,1,0,3,5]
list=sort(list)
print(list)
