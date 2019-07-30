from collections import deque


class BiTNode:
    def __init__(self):
        self.data=None
        self.lChild=None
        self.rChile=None
def arrayToTree(arr,start,end):
    root=None
    if end>=start:
        root=BiTNode()
        mid=int((start+end+1)/2)
        root.data=arr[mid]
        root.rChild=arrayToTree(arr,mid+1,end)
        root.lChild=arrayToTree(arr,start,mid-1)
    else:
        root=None
    return root
def midOder(root):
    if root==None:
        return
    if root.lChild!=None:
        midOder(root.lChild)
    print(root.data)
    if root.rChild!=None:
        midOder(root.rChild)
'''
逐层打印二叉树
'''
def printTreeLayer(root):
    if root==None:
        return None
    queue=deque()
    queue.append(root)
    while len(queue)>0:
        p=queue.popleft()
        print(p.data)
        if p.lChild!=None:
            queue.append(p.lChild)
        if p.rChild != None:
            queue.append(p.rChild)


arr=[1,2,3,4,5,6,7,8,9,10]
print(arr)
root=arrayToTree(arr,0,len(arr)-1)
printTreeLayer(root)