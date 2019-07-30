def isEqual(root1,root2):
    if root1==None and root2==None:
        return True
    elif root1!=None and root2!=None:
        if root1.data==root2.data:
            return isEqual(root1.lchild,root2.lchild) and isEqual(root1.rchild,root2.lchild)
    return False