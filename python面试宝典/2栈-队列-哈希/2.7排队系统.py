from collections import deque
class User:
     def __init__(self,id,name):
         self.id=id
         self.name=name
         self.seq=0
     def getName(self): return self.name
     def getSeq(self): return self.seq
     def getId(self): return  self.id
     def setName(self,name):   self.name=name
     def setId(self,id):   self.id=id
     def setSeq(self,seq):   self.seq=seq
     def equals(self,user1):
         return self.id==user1.id
     def toString(self):
         return  'id: '+str(self.id)+'    name: '+str(self.name)+'   seq: '+str(self.seq)
class MyQueue:
    def __init__(self):
        self.q=deque()
    def enQueue(self,u):
        u.setSeq(len(self.q)+1)
        self.q.append(u)
    def deQueue(self):
        self.q.popleft()
        self.updateSeq()
    def deQueuemove(self,u):
        self.q.remove(u)
        self.updateSeq()
    def updateSeq(self):
        i=1
        for  u in self.q:
            u.setSeq(i)
            i+=1
    def printfList(self):
        for u in self.q:
            print(u.toString())

u1=User(1,'user1')
u2=User(2,'user2')
u3=User(3,'user3')
u4=User(4,'user4')
queue=MyQueue()
queue.enQueue(u1)
queue.enQueue(u2)
queue.enQueue(u3)
queue.enQueue(u4)
queue.printfList()
queue.deQueue()
print('----------------------------')
queue.printfList()
queue.deQueuemove(u3)
print('----------------------------')
queue.printfList()