class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        top = False
        for i in range(1,len(arr)-1):
            if arr[i-1]<arr[i]<arr[i+1] and not top:
                continue
            elif arr[i-1] < arr[i] > arr[i+1] and not top:
                top = True
                continue
            elif arr[i-1] > arr[i] > arr[i+1] and top:
                continue
            else:
                return False
        
        if top:
            return True
        return False