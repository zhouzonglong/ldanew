import sys
'''
输入字典 {'a':1,'b':2,'c':3}
输出  a-1,b-2,c-3

巧妙的利用翻转！！！！！！！！！！！
'''

def printResult(Inputs):
    reverseInput=dict()
    for k,v in Inputs.items():
        reverseInput[v]=k
    start=None
    for k,v in Inputs.items():
        if k not  in reverseInput:
            start=k
            break
    if start==None:
        print('wrong input')
        return
    # print(start)
    to=Inputs[start]
    while to!=None:
        print(start+to)
        start=to
        try:
            to=Inputs[start]
        except:
            break
inputs=dict()
inputs['西安']='成都'
inputs['北京']='上海'
inputs['大连']='西安'
inputs['上海']='大连'
printResult(inputs)