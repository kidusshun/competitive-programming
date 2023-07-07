class Solution:
    def arrangeCoins(self, n: int) -> int:
        def isRowComplete(num,coins):
            val = (num*(num+1))//2
            return coins >= val

        l,r= 1,n

        while l<=r:
            mid = l + (r-l)//2
            if isRowComplete(mid,n):
                ans = mid
                l= mid +1
            elif not isRowComplete(mid,n):
                r= mid - 1
        return mid

s = Solution()
s.arrangeCoins(2)