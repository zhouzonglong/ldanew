class Test:
    def __init__(self):
        self.pos=0
    def partition(self,arr,low,high):
        key=arr[low]
        while low<high:
            while low<high and arr[high]>key:
                high-=1
            arr[low]=arr[high]
            while low<high and arr[low]<key:
                low+=1
            arr[high]=arr[low]
        arr[low]=key
        self.pos=low
    def getMid(self,arr):
        low=0
        n=len(arr)
        high=n-1
        mid=int((low+high)/2)
        while True:
            self.partition(arr,low,high)
            if self.pos==mid:
                break
            elif self.pos>mid:
                high=self.pos-1
            else:
                low=self.pos+1
        print(arr)
        print(mid)
        return arr[mid] if (n%2)!=0 else (arr[mid]+arr[mid+1])/2
arr=[7,9,3,5,1,11]
print(Test().getMid(arr))