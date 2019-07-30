import numpy as np
import sys
'''
求能被2或3或5整除的第1500个数，a1=1
'''
'''
蛮力法：不提倡
'''
def get1500(n):
    i=1
    list=[]
    count=0
    while True:
        if i%2==0 or i%3==0 or i%5==0:
            count+=1
            list.append(i)
        if count==n:
            break
        i+=1
    return list
list=get1500(1500)
a=np.array(list)
# b=a.reshape(5,300)
print(a)


'''
# x/2+x/3+x/5-x/6-x/10-x/15+x/30=1500

2040/2 = 1020   ....2040前有1020个能被2整除的数
2040/3 = 680  ....2040前有1020个能被3整除的数 
2040/5 = 408 ....2040前有1020个能被5整除的数 
2040/6 = 340 ....2040前有1020个能被6整除的数（2和3的最小公倍数为6） 
2040/10 = 204 ....2040前有1020个能被10整除的数（2和5的最小公倍数为10）  
2040/15 = 136 ....2040前有1020个能被15整除的数（3和5的最小公倍数为15）        
2040/30 = 68 ....2040前有1020个能被30整除的数 （2、3、5的最小公倍数为30）       
那么1020+680+408-340-204-136+68=1496（说明2040是该数列中的第1497个元素（加上第一个元素1））
所以第1498是2042，第1499是2043，第1500是2044  
'''
def searth2(n):
    return int(n*15/11)

'''
利用周期性，最小公倍数为30，周期30内的数有22个䏻被2、3、5整除
1500/22=68.....4 第68周期第4个数
'''
def searth(n):
    a=[0,2,3,4,5,6,8,9,10,12,14,15,16,18,20,21,22,24,25,26,27,28,30]
    ret=int(n/22)*30+a[n%22]
    return ret

# print(searth2(30))