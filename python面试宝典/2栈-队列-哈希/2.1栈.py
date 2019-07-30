import sys
'''
数组形式的栈
'''
class MyStack:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return len(self.items)==0
    def size(self):
        return len(self.items)
    def top(self):
        if not self.isEmpty():
            return  self.items[len(self.items)-1]
        else:
            return None
    def pop(self):
        if len(self.items)>0:
            return self.items.pop()
        else:
            print('empty')
            return None
    def push(self,item):
        self.items.append(item)
# s=MyStack()
# s.push(4)
# print(s.top())
# print(s.size())
# s.pop()
# print(s.size())

'''
链表形式的栈
'''
class LNode:
    def __init__(self,x):
        self.data=x
        self.next=None
class MyStackLink:
    def __init__(self):
        self.data=None
        self.next=None
    def empty(self):
        if self.next==None:
            return True
        return False
    def size(self):
        size=0
        p=self.next
        while p!=None:
            size+=1
            p=p.next
        return size
    def push(self,e):
        p=LNode
        p.data=e
        p.next=self.next
        self.next=p
    def pop(self):
        self.next=self.next.next
        # tem=self.next
        # if tem!=None:
        #     self.next=tem.next
        #     return tem.data
        # else:
        #     print('empty')
        #     return None
    def top(self):
        if self.next!=None:
            return self.next.data
        else:
            print('empty')
            return None
s=MyStack()
s.push(4)
s.push(2)
s.push(5)
print(s.top())
s.pop()
print(s.top())
