# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l,r = 1,n
        while l<=r:
            curr = (l+r)//2
            if isBadVersion(curr):
                r = curr - 1
            else:
                l = curr + 1
        return l