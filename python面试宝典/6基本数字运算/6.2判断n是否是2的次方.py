import sys
'''
方法一：移位操作
'''
def ispower(n):
    i=1
    while i<=n:
        if i==n:
            return True
        i<<=1
    return  False
print(ispower(7))


'''
方法二：
n-1和n进行与操作
'''
def isPower(n):
    if n<1:
        return False
    m=n-1
    if m&n==0:
        return True
    return False
print(isPower(5))
