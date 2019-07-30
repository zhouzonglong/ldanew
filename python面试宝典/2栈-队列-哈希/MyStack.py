class MyStack1:
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