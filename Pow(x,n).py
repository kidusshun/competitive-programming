class Solution:
    def myPow(self, x: float, n: int) -> float:
        k=abs(n)
        if k == 0:
            return 1
        elif k % 2 == 0:
            res= self.myPow(x * x, k // 2)
        else:
            res= x * self.myPow(x * x, (k - 1) // 2)

        
        return float(res) if n >= 0 else 1/res
s=Solution()
print(s.myPow(2.10000,3))