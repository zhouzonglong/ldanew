# import bitmap as bitmap
#
#
# def getbit(phone):
#     bitmap[phone/(8*4)]|=1<<(phone%(8*4))
#     return bitmap[phone/(8*4)]
# num=13135445678
# print(getbit(num))
# 初始化bitmap
import time


class Bitmap():
    def __init__(self, max):
        """确定数组个数"""
        self.size = int((max + 31 - 1) / 31)
        # max需要传入的为要排序的最大数
        self.array = [0 for i in range(self.size)]

    def bitindex(self, num):
        """确定数组中元素的位索引"""
        return num % 31

    def set_1(self, num):
        """将元素所在的位——置1"""
        elemindex = (num // 31)  # 整除，否则为浮点值
        byteindex = self.bitindex(num)
        ele = self.array[elemindex]
        self.array[elemindex] = ele | (1 << byteindex)

    def test_1(self, i):
        elemindex = (i // 31)  # 整除，否则为浮点值
        byteindex = self.bitindex(i)
        if self.array[elemindex] & (1 << byteindex):
            return True
        return False


# if __name__ == '__main__':
#     Max = ord('z')  # ord('*')返回单字符在ASCII中对应的整数
#     shuffle_array = [x for x in 'qwelajkda']
#     ret = []
#     bitmap = Bitmap(Max)
#     for c in shuffle_array:
#         bitmap.set_1(ord(c))
#     for i in range(Max + 1):
#         if bitmap.test_1(i):
#             ret.append(chr(i))
#     print(u'原始数组是:%s' % shuffle_array)
#     print(u'排序以后的数组是:%s' % ret)



def BitSort(str):
    bit=[0]*100
    j=0
    for i in range(0,len(str)):
        bit[str[i]]=1
      for i in range(0,len(bit)):
          if bit[i]==1:
            str[j]=i
            j+=1
str=[49,27,32,3,38,1,13,76,97,65] #测试数据需要唯一
beginTime=time.clock()
BitSort(str)
endTime=time.clock()
print("位图排序")
print(str)
print(endTime-beginTime)
