class Stack:
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
class MyStack:
    def __init__(self):
        self.elemStack=Stack()
        self.minStack=Stack()
    def push(self,data):
        self.elemStack.push(data)
        if self.minStack.isEmpty():
            self.minStack.push(data)
        else:
            if self.minStack.top() >data:
                self.minStack.push(data)
    def pop(self):
        topdata=self.elemStack.pop()
        if topdata==self.minStack.top():
            self.minStack.pop()
        return topdata
    def mins(self):
        if self.minStack.isEmpty():
            print('wu')
        else:
            print(self.minStack.top())

stack=MyStack()
stack.push(2)
stack.mins()
stack.push(1)
stack.mins()
stack.pop()
stack.mins()

