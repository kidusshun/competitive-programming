# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        l,r=1,n
        while l<=r:
            curr = (l+r)//2
            guessed =guess(curr)
            if guessed == 0:
                return curr
            elif guessed == -1:
                r = curr -1 
            else:
                l = curr +1