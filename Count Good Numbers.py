class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod=10**9+7
        num_odds=n//2
        if n%2==0:
            num_evens=n//2
        else:
            num_evens=n//2 + 1
            
        even = pow(5,num_evens,mod)      
        odd = pow(4,num_odds,mod)      
        return (even * odd) % mod
	