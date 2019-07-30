import sys
'''
中心扩展
会问字符串
'''
class Test:
    def __init__(self):
        self.startIndex=0
        self.lens=0
    def getStartIndex(self):return self.startIndex
    def getLen(self):return  self.lens

    #对字符串str以c1和c2位中心向外扩展
    def expandBothside(self,strs,c1,c2):
        n=len(strs)
        while c1>0 and c2<n and list(strs)[c1]==list(strs)[c2]:
            c1-=1
            c2+=1
        temStartIndex=c1+1
        tempLen=c2-c1-1
        print('---------'+str(tempLen))
        if tempLen>self.lens:
            self.lens=tempLen
            self.startIndex=temStartIndex
    def getLongestPalindrome(self,strs):
        if strs==None:
            return
        n=len(strs)
        if (n<1):
            return
        i=0
        while i<n-1:
            #找出回文字符串的长度为奇数的情况
            self.expandBothside(strs,i,i)
            #找出回文字符串的长度为偶数数的情况
            self.expandBothside(strs,i,i+1)
            i+=1
strs='abcefgfedxyzffd'
t=Test()
t.getLongestPalindrome(strs)
if t.getStartIndex()!=-1 and t.getLen()!=-1:
    print('the most length str is:\n')
    i=t.getStartIndex()
    print(t.getLen())
    print(strs)
    while i<t.getStartIndex()+t.getLen():
        print(list(strs)[i])
        i+=1
else:
    print('false')
