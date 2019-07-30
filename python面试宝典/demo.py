import math

import numpy as np
# M=[[0]*3]*4
# print(M)
# M=[([0]*(3)) for i in range(4)]
# print(M)

# M[1][1]=1
# print(M)
# dex=np.zeros((3,3))
# dex[2][1]=4
# print(dex)

# a=1
# list=[2,3,4,5]
# for each in list:
#     a^=each
#     print(str(a)+'*****'+str(each))
#

# dic={'a':2,'b':4,'c':3}
# for k,v in dic.items():
#     print(k)


# a=2
# b=3
# # c=5
# x=a^b
# print(x)
# print(x^b)

#100 4
#101 5
# print(5>>1)
# import sys
# print(sys.getdefaultencoding())

# print(math.log(8,2))



#!/usr/bin/python
# -*- coding: UTF-8 -*-
# import pymysql
#
# # 打开数据库连接|
# db = pymysql.connect("localhost", "root", "123123", "qq", charset='utf8' )
#
# # 使用cursor()方法获取操作游标
# cursor = db.cursor()
#
# '''
# 问题：
# 1、由于字符的原因比如“8°C”或者德文字符“Ä,Ö,ü”
#     解决方法：
#         1、字符替换（“°”转换为“。”，“—”转换为“-”）
#         2、改变编码格式
# 2、由于数据库字段的限制（某些字段只能够存储20字符）
#     解决方法：
#         1、修改字段存储长度
#         2、忽略掉
# '''
# # 使用execute方法执行SQL语句
# sql="INSERT INTO users (ID,Name,Pwd) values(486,'8° S','jack')"
# cursor.execute(sql)
# db.commit()
# # 使用 fetchone() 方法获取一条数据
# data = cursor.fetchone()
#
# print (data)
#
# # 关闭数据库连接
# db.close()




visited=[None]*5
visited[2]=False
print(visited)











