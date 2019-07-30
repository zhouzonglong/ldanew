# N**2=1+3+5+7+...+(2*n-1)
def isPower(n):
    dex=1
    while n>0:
        n=n-dex
        if n==0:
            return 'true'
        elif n<0:
            return 'false'
        else:
            dex+=2
    return 'false'
print(isPower(9))
