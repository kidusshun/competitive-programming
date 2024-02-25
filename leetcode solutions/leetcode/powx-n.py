class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        new_n = abs(n)
        def helper(x,n,c):
            if n == 1:
                return x,c
            return helper(x*x, n//2,c+1)
        
        val,c =  helper(x,new_n,0)
        left =new_n - pow(2,c)
        val *= pow(x,left)
        if n <0:
            return 1/val
        
        return val
            