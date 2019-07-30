class LNode:
    def __init__(self,x):
        self.data=x
        self.next=None
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
def isPop(push,pop):
    pushLen=len(push)
    popLen=len(pop)
    if pushLen!=popLen:
        return False
    pushIndex=0
    popIndex=0
    stack=MyStack()
    while pushIndex<pushLen:
        stack.push(push[pushIndex])
        pushIndex+=1
        while (not stack.isEmpty()) and stack.top()==pop[popIndex]:
            stack.pop()
            popIndex+=1
    return stack.isEmpty() and popLen==popIndex
push='12345'
pop='54321'
if isPop(push,pop):
    print('yes')
else:
    print('no')

