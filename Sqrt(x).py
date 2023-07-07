class Solution:
    def mySqrt(self, x: int) -> int:
        arr=[]
        for i in range(1,x+1):
            arr.append(i)
        
        l,r=0,len(arr)-1

        while l<=r:
            mid = l +(r-l)//2
            if arr[mid]**2 <x:
                l=mid+1
            elif arr[mid]**2 >x:
                r=mid-1
            else: return arr[mid]
        
        if arr[mid]**2 > x: return arr[mid-1]
        else: return arr[mid]

s = Solution()
s.mySqrt(4)