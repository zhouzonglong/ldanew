class CommonSubString():
    def maxprefix(self,s1,s2):
        i=0
        while i<len(s1) and i<len(s2):
            if list(s1)[i]==list(s2)[i]:
                i+=1
            else:
                break
            i+=1
        return i
    def getMaxCommonStr(self,txt):
        n=len(txt)
        suffixes=[None]*n
        longstrlen=0
        longstr=None
        i=0
        while i<n:
            suffixes[i]=txt[i:]
            i+=1
        suffixes.sort()
        i=1
        while i<n:
            tmp=self.maxprefix(suffixes[i],suffixes[i-1])
            if tmp>longstrlen:
                longstrlen=tmp
                longstr=suffixes[i][0:i+1]
            i+=1
        return longstr
txt='banana'
c=CommonSubString()
print(c.getMaxCommonStr(txt))