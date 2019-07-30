from collections import deque


class BiTNode:
    def __init__(self):
        self.data=None
        self.lchild=None
        self.rchild=None
    # def isEqual(self,root1,root2):
class Test:
    def __init__(self):
        self.maxSum=-2**31
    def findMaxSubTree(self,root,maxRoot):
        if root==None:
            return 0
        lmax=self.findMaxSubTree(root.lchild,maxRoot)
        rmax=self.findMaxSubTree(root.rchild,maxRoot)
        sums=lmax+rmax+root.data
        if sums>self.maxSum:
            self.maxSum=sums
            maxRoot.data=root.data
        return sums

    def printTreeLayer(self,root):
        if root == None:
            return None
        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            p = queue.popleft()
            print(p.data)
            if p.lchild != None:
                queue.append(p.lChild)
            if p.rchild != None:
                queue.append(p.rChild)
    def constructTree(self):
        root=BiTNode()
        node1=BiTNode()
        node2 = BiTNode()
        node3 = BiTNode()
        node4 = BiTNode()
        node5 = BiTNode()
        node6 = BiTNode()
        # node1 = BiTNode()
        root.data=-14
        root.lchild=node1
        root.rchild=node2
        node1.data=4
        node2.data=5
        node3.data=4
        node4.data=4
        node5.data=5
        node6.data=5
        node1.lchild=node3
        node1.rchild=node4
        node2.lchild = node5
        node2.rchild = node6
        node3.rchild=node3.lchild=node4.rchild=node4.lchild=node5.rchild=node5.lchild=node6.rchild=node6.lchild=None
        return root
test=Test()
root=test.constructTree()
maxRoot=BiTNode()
test.findMaxSubTree(root,maxRoot)
print(test.maxSum)
print(maxRoot.data)
test.printTreeLayer(maxRoot)