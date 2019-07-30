import sys
'''
计算N!后有零的个数：N/5+N/5^2+N/5^3+……+
'''
def zeroCount(n):
    count=0
    while n>1:
        n=int(n/5)       #记得取整
        print(n)
        count+=n
    return count
print(zeroCount(1024))