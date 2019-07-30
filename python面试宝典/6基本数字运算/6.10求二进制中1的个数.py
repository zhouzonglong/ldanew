'''
方法一：移位法
'''
def getCount(n):
    count=0
    while n>0:
        if (n&1)==1:
            count+=1
        n=n>>1
    return count
print(getCount(10))


'''
方法二：与操作      n&(n-1)---->使得n的二进制1少一个
'''
def get_count(n):
    count=0
    while n>0:
        if n!=0:
            n=n&(n-1)
        count+=1
    return count
print(get_count(10))
