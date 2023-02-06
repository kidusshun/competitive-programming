class Solution: 
    def select(self, arr, i):
        # code here 
        return arr[i]
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            min_index=i
            smallest=arr[i]
            for j in range(i+1,n):
                if arr[j]<smallest:
                    min_index=j
                    smallest=arr[j]
            self.select(arr,i)
            arr[i],arr[min_index]=arr[min_index],arr[i]
        return arr