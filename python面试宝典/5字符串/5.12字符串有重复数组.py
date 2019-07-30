'''
方法一：字典
'''
'''
方法二：bit
'''
def isDup(strs):
    lens=len(strs)
    flage=[0,0,0,0,0,0,0,0]
    i=0
    while i<lens:
        index=int(ord(list(strs)[i])/32)
        shift=ord(list(strs)[i])%32
        if (flage[index]&(1<<shift))!=0:
            return True
        flage[index]|=(1<<shift)
        i+=1 
    return False
print(isDup('rtte'))