class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        num_piles = len(piles)//3
        i = len(piles) - 2
        ans = 0
        while num_piles >0:
            ans+=piles[i]
            i-=2
            num_piles-=1
        return ans