from collections import  deque
class LRU:
    def __init__(self,cacheSize):
        self.cacheSize=cacheSize
        self.queue=deque()
        self.hashSet=set()
    def isQueueFull(self):
        return len(self.queue)==self.cacheSize
    def enQueue(self,pageNum):
        #调整队列，若队列满删除再添加

        if self.isQueueFull():
            tem=self.queue[-1]
            self.queue.remove(tem)
            self.hashSet.remove(tem)
        self.queue.appendleft(pageNum)
        self.hashSet.add(pageNum)
    def accessPage(self,pageNum):
        if pageNum not in self.hashSet:
            self.enQueue(pageNum)
        if pageNum != self.queue[0]:
            self.queue.remove(pageNum)
            self.queue.appendleft(pageNum)


    # def accessPageNum(self,pageNum):
    #     if pageNum not in self.hashSet:
    #         self.enQueue(pageNum)
    #     elif pageNum != self.queue[0]:
    #         self.queue.remove(pageNum)
    #         self.queue.appendleft(pageNum)
    def printQueue(self):
        print(self.hashSet)
        while len(self.queue)>0:
            print(self.queue.popleft())
lr=LRU(3)
lr.accessPage(1)
lr.accessPage(2)
lr.accessPage(5)
lr.accessPage(1)
lr.accessPage(6)
lr.accessPage(7)
lr.printQueue()
