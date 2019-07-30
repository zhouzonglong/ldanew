'''
要求4不在第三位，3,5不相邻
'''
'''
采用图的方式
'''
class Test:
    def __init__(self,arr):
        self.number=arr  #arr=[1,2,2,3,4,5]
        self.visited=[None]*len(self.number)
        self.graph=[[None]*len(self.number) for i in range(len(self.number))]
        self.n=6
        # self.visited=None
        # self.graph=None
        self.combination=''
        self.s=set()
    def depthFirstSearch(self,start):
        self.visited[start]=True
        self.combination+=str(self.number[start])
        if len(self.combination)==self.n:
            if self.combination.index('4')!=2:
                self.s.add(self.combination)
        j=0
        while j<self.n:
            if self.graph[start][j]==1 and self.visited[j]==False:
                self.depthFirstSearch(j)
            j+=1
        self.combination=self.combination[:-1]
        self.visited[start]=False
    def getAllCombination(self):
        i=0
        while i<self.n:
            j=0
            while j<self.n:
                print(self.graph[i][j])
                if i==j:
                    print(self.graph[i][j])
                    self.graph[i][j]=0
                else:
                    self.graph[i][j]=1
                j+=1
                i+=1
            self.graph[3][5]=0
            self.graph[5][3]=0
            i=0
            while i <self.n:
                self.depthFirstSearch(i)
                i+=1
    def printAll(self):
        for strs in self.s:
            print(strs)
arr=[1,2,2,3,4,5]
t=Test(arr)
t.getAllCombination()
t.printAll()