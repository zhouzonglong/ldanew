import sys

from numpy import long

'''
divmod(7,2)结果返回商和余数
'''
def intToBaiary(n):
    hexNum=8*8
    bit=[]
    for i in range(hexNum):
        b=n>>i
        c,d=divmod(b,2)
        bit.append(str(d))
        print(d)
    return ''.join(bit[::-1])
# print(intToBaiary(long(10)))
def intToHex(s):
    hexs=''
    remainder=0
    while s!=0:
        remainder=s%16
        if remainder<10:
            hexs=str(remainder+int('0')+hexs)
        else:
            hexs=str(remainder-10+ord('A'))+hexs
        s=s>>4
    return chr(int(hexs))
list=intToHex(10)
print(list)


def intToBaiary2(n):
    hexNum=8*8
    bit=[]
    for i in range(hexNum):
        b=n>>i
        c,d=divmod(b,2)
        bit.append(str(d))
    return bit[::-1]
def intToHex2(n):
    a=intToBaiary2(n)
    list=[]
    i=len(a)
    # print(str(i)+'----------------------')
    while i>=4:
        a1=a[i-4:i]
        # print(a1)
        A1 = (int(a1[0]) << 3) + (int(a1[1]) << 2) + (int(a1[2])<< 1) + int(a1[3])
        # print(A1)
        if A1>=10:
            if A1==10:
                list.append('A')
            elif A1 == 11:list.append('B')
            elif A1==12:list.append('C')
            elif A1==13:list.append('D')
            elif A1 == 13:list.append('D')
            elif A1 == 14: list.append('D')
            else : list.append('D')
        else:
            list.append(str(A1))
        i-=4
    return  list[::-1]

# print(0<<3)