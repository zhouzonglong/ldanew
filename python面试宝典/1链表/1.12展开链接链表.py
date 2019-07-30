'''
3->4->6->6
|  |  |  |
5  6  2  1
   |     |
   2     7
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.down=None
class MergeList:
    def __init__(self):
        self.head=None
    def merge(self,a,b):
        if a==None:
            return b
        if b==None:
            return a
        if a.data<b.data:
            result=a
            result.down=self.merge(a.down,b)
        else:
            result=b
            result.dowm=self.merge(a,b.down)
        return result
    def flatten(self,root):
        if root==None or root.right==None:
            return root
        root.right=self.flatten(root.right)
        root=self.merge(root,root.right)
        return root
    def insert(self,head_ref,data):
        new_node=Node(data)
        new_node.down=head_ref
        head_ref=new_node
        return head_ref
    def printList(self):
        temp=self.head
        while temp!=None:
            print(temp.data)
            temp=temp.down
            # print('\n')
if __name__=='__main__':
    L=MergeList()
    L.head = L.insert(L.head,31)
    L.head = L.insert(L.head, 8)
    L.head = L.insert(L.head, 6)
    L.head = L.insert(L.head, 3)
    L.head.right=L.insert(L.head.right,21)
    L.head.right = L.insert(L.head.right, 11)
    L.head.right.right = L.insert(L.head.right.right, 50)
    L.head.right.right = L.insert(L.head.right.right, 22)
    L.head.right.right = L.insert(L.head.right.right, 15)
    L.head.right.right.right = L.insert(L.head.right.right.right, 55)
    L.head.right.right.right = L.insert(L.head.right.right.right, 40)
    L.head.right.right.right = L.insert(L.head.right.right.right, 39)
    L.head.right.right.right = L.insert(L.head.right.right.right, 30)
    # L.printList()
    L.head=L.flatten(L.head)
    # L.head=merge()
    L.printList()

