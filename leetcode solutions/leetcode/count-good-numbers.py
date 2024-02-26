class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9+7
        odds = n//2
        evens = n-odds
        
        def calculate(x,n):
            if n == 0:
                return 1
            if n%2 == 0:
                return calculate((x*x)%mod,  n//2)
            else:
                return x* calculate((x*x)%mod, (n-1)//2)
        
        return (calculate(5,evens) * calculate(4,odds))%mod
