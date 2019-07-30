import sys
'''
数组方法
'''
class MyQueu:
    def __init__(self):
        self.arr=[]
        self.front=0
        self.rear=0
    def isEmpty(self):
        return self.front==self.rear
    def size(self):
        return self.rear-self.front
    def getFront(self):
        if self.isEmpty():
            print('empty')
            return None
        else:
            return self.arr[self.front]
    def getBack(self):
        if self.isEmpty():
            print('empty')
            return None
        else:
            return self.arr[self.rear-1]
    def deQueue(self):
        if self.rear>self.front:
            self.front+=1
        else:
            print('empty')
    def addQueue(self,e):
        self.arr.append(e)
        # self.arr[self.rear+1]=e
        self.rear+=1
# queue=MyQueu()
# queue.addQueue(2)
# print(queue.size())
# print(queue.getFront())
# queue.deQueue()
# print(queue.size())
'''
链表方法
'''
class LNode:
    def __new__(self, x):
        self.data=x
        self.next=None
class MyQueue2:
    def __init__(self):
        self.pHead=None
        self.pEnd=None
    def empty(self):
        if self.pHead==None:
            return True
        else:
            return False
    def size(self):
        size=0
        p=self.pHead
        while p!=None:
            p=p.next
            size+=1
        return size
    def enQueue(self,e):
        p=LNode
        p.data=e
        p.next=None
        if self.pHead==None:
            self.pHead=self.pEnd=p
        else:
            self.pEnd.next=p
            self.pEnd=p
    def getFront(self):
        if self.pHead==None:
            return None
        else:
            return self.pHead.data
    def getBack(self):
        if self.pEnd==None:
            return None
        else:
            return self.pEnd.data
    def deQueue(self):
        if self.pHead==None:
            print('empty')
        self.pHead=self.pHead.next
        if self.pHead==None:
            self.pEnd=None
queue=MyQueue2()
queue.enQueue(2)
print(queue.size())
print(queue.getFront())
queue.deQueue()
print(queue.size())