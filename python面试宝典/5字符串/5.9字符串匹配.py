import sys
'''
判断p是否是s的字串，是则返回位置
方法一：直接计算
'''
# def match(s,p):
#     #判断两个串为None吗
#     slen=len(s)
#     plen=len(p)
#     if slen<plen:
#         return -1
#     i=0
#     j=0
#     while i<slen and j<plen:
#         if(list(s)[i]==list(p)[j]):
#             print('---------------i:'+str(i)+'   j:'+str(j))
#             i+=1
#             j+=1
#         else:
#             i=i-j+1
#             j=0
#             print('i:'+str(i)+'   j:'+str(j))
#             if(i>slen-plen):
#                 return  -1
#     if j>=plen:
#         return i-plen
#     return  -1
# print(match('sfdabdeeabcsdhhk','abc'))


'''
判断p是否是s的字串，是则返回位置
方法一：kmp算法
'''
def getNext(p,nexts):
    i=0
    j=-1
    nexts[0]=-1
    while i<len(p):
        if j==-1 or list(p)[i]==list(p)[j]:
            i+=1
            j+=1
            nexts[i]=j
        else:
            j=nexts[j]
def match(s,p,nexts):
    #保证输入的字串p小于母串s
    if s==None or p==None:
        return -1
    slen=len(s)
    plen=len(p)
    if slen<plen:
        return -1
    i=0
    j=0
    while i<slen and j<plen:
        print('i='+str(i)+'  j='+str(j))
        if j==-1 or list(s)[i]==list(p)[j]:
            i+=1
            j+=1
        else:
            j=nexts[j]
    if j>=plen:
        return  i-plen
    return  -1


s='abababaabcbab'
p='abaabc'
lens=len(p)
nexts=[0]*(lens+1)
getNext(p,nexts)
print('nexts数组为：'+str(nexts[0]))
i=1
while i<lens-1:
    print(','+str(nexts[i]))
    i+=1
print('\n')
print('匹配结果为：'+str(match(s,p,nexts)))




