import  MyStack

def moveBottomToTop(s):
    if s.isEmpty():
        return
    top1=s.top()
    s.pop()
    if not s.isEmpty():
        # 递归处理不包括栈顶元素的子站
        moveBottomToTop(s)
        top2=s.top()
        s.pop()
        s.push(top1)
        s.push(top2)
    else:
        s.push(top1)
def reverse_stack(s):
    if s.isEmpty():
        return
    moveBottomToTop(s)
    top=s.top()
    s.pop()
    reverse_stack(s)
    s.push(top)

s=MyStack.MyStack1()
s.push(5)
s.push(4)
s.push(3)
s.push(2)
s.push(1)
while not s.isEmpty():
    print(s.top())
    s.pop()
s.push(5)
s.push(4)
s.push(3)
s.push(2)
s.push(1)
reverse_stack(s)
while not s.isEmpty():
    print(s.top())
    s.pop()
 # ================================================栈排序==============================================================
def moveBottomToTop(s):
    if s.isEmpty():
        return
    top1 = s.top()
    s.pop()
    if not s.isEmpty():
        # 递归处理不包括栈顶元素的子站
        moveBottomToTop(s)
        top2 = s.top()
        if top1>top2:
            s.pop()
            s.push(top1)
            s.push(top2)
    else:
        s.push(top1)


def sort_stack(s):
    if s.isEmpty():
        return
    moveBottomToTop(s)
    top = s.top()
    s.pop()
    reverse_stack(s)
    s.push(top)