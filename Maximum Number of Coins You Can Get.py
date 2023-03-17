class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        max=0
        count=0
        for i in range(len(piles)-2,0,-2):
            if count<len(piles)//3:
                max+=piles[i]
            count+=1
        return max