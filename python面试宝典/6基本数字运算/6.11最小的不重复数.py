'''
比1121大的最小不重复数（邻位不相同）
'''
def getList(n):
    list = []
    while n > 0:
        m = n % 10
        list.append(m)
        n = int(n / 10)
    list.append(0)
    list.reverse()
    return list
def isfu(n):
    list=getList(n)
    for i in range(len(list)-1):
            if list[i+1]==list[i]:
                return  True
    return False
def getn(list):
    # print(list)
    num=0
    length=len(list)-1
    for i in range(0,len(list)):
        # print(list[i]*pow(10,length-i))
        num+=list[i]*pow(10,length-i)
    return  num
def getNum(n):
    Num=n+1
    while isfu(Num):
        list = getList(Num)
        for i in range(len(list)-1):
            if list[i]==list[i+1]:
                list[i+1]+=1
                if list[i+1]==10:
                    list[i]+=1
                    list[i+1]=0
                while i<len(list):
                    list[i]=0
        Num = getn(list)
    return Num


print(getNum(21))