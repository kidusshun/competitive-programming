class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        l,r=0,x

        while l<=r:
            mid = l +(r-l)//2
            if mid**2 <x:
                l=mid+1
            elif mid**2 >x:
                r=mid-1
            else: return mid
        
        if mid**2 > x: return mid-1
        else: return mid