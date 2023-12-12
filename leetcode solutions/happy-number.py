class Solution:
    def isHappy(self, n: int) -> bool:
        if n < 10:
            if n %2 == 0 or n==3 or n==5 or n==9:
                return False
            else:
                return True
        
        curr = 0
        for digit in str(n):
            curr += int(digit)**2
        return self.isHappy(curr)