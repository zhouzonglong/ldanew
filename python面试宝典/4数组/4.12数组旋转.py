'''
二维数组n*n，逆时针旋转45度
'''
def rotataArr(arr):
    length=len(arr[0])
    print(length)
    j=length-1
    while j>0:
        i1=0
        k1=j
        list = []
        while True:
            if i1< length and k1<length:
                list.append(arr[i1][k1])
                # print(arr[i][j])
                i1 +=1
                k1 +=1
            else:
                break
        print("".join(str(list)))
        j-=1
    i=0
    while i<length:
        i1 = i
        k1 = 0
        list = []
        while True:
            if i1< length and k1<length:
                list.append(arr[i1][k1])
                # print(arr[i][j])
                i1 +=1
                k1 +=1
            else:
                break
        print("".join(str(list)))
        i+=1

arr=[[1,2,3],[4,5,6],[7,8,9]]
print(arr)
rotataArr(arr)