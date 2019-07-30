'''
牛顿法
'''
def s(n):
    #最好的用牛顿迭代法,19只需要6次
    if n<0:
        return -1
    else:
        start=1
        while  abs((start*start-n))>1e-9:
            start=(start+n/start)/2.0
        return start
print(s(64))

'''
二分法 
'''
def s(n):
    #二分法,构造函数f(x)=x*x-n,然后构造上下界[1,n]，比较mid=(start+end)/2.0，比较mid*mid-n和极小值的大小1e-9，\
    #如果大于0，则将上界变小，end=mid，如果小于0，说明mid小于正确值，应该将下界变大，start=mid
    #19只需要36次
    i=0
    if n<0:
        return -1
    else:
        start=1
        end=n
        mid=(start+end)/2.0
        while (mid*mid-n)>1e-9 or ((mid*mid-n)<-(1e-9)):
            i=i+1
            print (i,mid)
            if (mid*mid-n>1e-9):
                end=mid
            elif(mid*mid-n<-1e-9):
                start=mid
            mid=(start+end)/2.0
            print (i,mid)
    return mid

