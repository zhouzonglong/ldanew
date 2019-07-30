import sys
'''
通过双倍的字符长度来确定是否是旋转的
'''
def haves(strlong,strshort):
    return  strlong.find(strshort)!=-1
def ifCan(str1,str2):
    # 判断是否空
    strs=str1+str1
    if haves(strs,str2):
        print('True')
    else:
        print('no')
ifCan('hgfdjshjisdh','jsh')