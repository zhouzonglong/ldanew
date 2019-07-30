import sys
'''
方法一：双重循环
'''
class LNode:
    def __init__(self,x):
        self.data=x
        self.next=None
def printNode(head):
    cur=head.next
    while cur!=None:
        print(cur.data)
        cur=cur.next
def creatLinks():
    i = 1
    head = LNode(0)
    head.next = None
    tmp = None
    cur = head
    # 构建链表
    while i < 7:
        tmp = LNode(0)
        if i%2==0:
            tmp.data = i+1
        elif i%3==0:
            tmp.data=i-2
        else:
            tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1
    return  head
def delNode(head):
    tem=head.next
    while tem.next!= None:
        pre=tem
        cur=tem.next
        while cur!=None:
            if cur.data==tem.data:
                pre.next=cur.next
                cur=pre.next
            else:
                pre=pre.next
                cur=cur.next
        tem=tem.next
    return head



def main1():
    head=creatLinks()
    print('逆序前------------------')
    printNode(head)
    print(head.next)
    print(id(head.next))

    print('逆序后=========================')
    head=delNode(head)
    printNode(head)

main1()

'''
方法二使用list存储。空间换时间
'''
# 有删，无添加到list中


