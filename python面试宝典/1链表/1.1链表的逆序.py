import sys
'''
方法一：利用指针倒着指向逆序（只有一个元素的时候报错）
'''
class LNode:
    # def __new__(self,x):
    #     self.data=x
    #     self.next=None
    def __init__(self,x):
        self.data=x
        self.next=None

def Reverse(head):
    if head==None or head.next==None:
        return
    pre=None
    cur=None
    next=None
    #把链表的首节点变成尾节点
    cur=head.next
    next=cur.next
    cur.next=None
    pre=cur
    cur=next
    while cur.next!=None:
        next=cur.next
        cur.next=pre
        pre=cur
        cur=next
    #链表的最后一个节点指向倒数第二个节点
    cur.next=pre
    #链表的头结点之指向原来的尾节点
    head.next=cur
def main1():
    i=1
    head=LNode(0)
    head.next=None
    tmp=None
    cur=head
    #构建链表
    while i<3:
        tmp=LNode(0)
        tmp.data=i
        tmp.next=None
        cur.next=tmp
        cur=tmp
        i+=1
    print('逆序前------------------')
    cur=head.next
    while cur!=None:
        print(cur.data)
        cur=cur.next
    print('逆序后-==========================')
    Reverse(head)
    cur=head.next
    while cur!=None:
        print(cur.data)
        cur=cur.next


'''
方法二：递归
'''
def  RecuisiceReverse(head):
    if head is None or head.next is None:
        return head
    else:
        newhead=RecuisiceReverse(head.next)
        head.next.next=head
        head.next=None
    return  newhead

def Reverse2(head):
    if head is None:
        return
    firstNone=head.next
    newhead=RecuisiceReverse(firstNone)
    head.next=newhead
    return newhead
def main2():
    i=1
    head=LNode(0)
    head.next=None
    tmp=None
    cur=head
    #构建链表
    while i<5:
        tmp=LNode(0)
        tmp.data=i
        tmp.next=None
        cur.next=tmp
        cur=tmp
        i+=1
    print('逆序前------------------')
    cur=head.next
    while cur!=None:
        print(cur.data)
        cur=cur.next
    print('逆序后=========================')
    Reverse2(head)
    cur=head.next
    while cur!=None:
        print(cur.data)
        cur=cur.next
# main2()
'''
方法三：插入法
'''
def Reverse3(head):
    if  head.next.next is None:
        return head
    else:
        next = None
        cur=head.next.next
        head.next.next=None
        while cur is not None:
            next = cur.next
            cur.next = head.next
            head.next = cur
            cur = next
    return head
def main3():
    i=1
    head=LNode(0)
    head.next=None
    tmp=None
    cur=head
    #构建链表
    while i<7:
        tmp=LNode(0)
        tmp.data=i
        tmp.next=None
        cur.next=tmp
        cur=tmp
        i+=1
    print('逆序前------------------')
    cur=head.next
    while cur!=None:
        print(cur.data)
        cur=cur.next
    print('逆序后=========================')
    Reverse3(head)
    cur=head.next
    while cur!=None:
        print(cur.data)
        cur=cur.next
main3()










class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None






