def bubble_sort(list):
    count=len(list)
    for i in range(0,count):
        for j in range(i+1,count):
            if(list[i]>list[j]):
                list[i],list[j]=list[j],list[i]
                return list

list=[3,5,2,0,9,6,1]
print(bubble_sort(list))
