def maxCoins(piles: list[int]) -> int:
        piles.sort()
        max=0
        count=0
        for i in range(len(piles)-2,0,-2):
            if count<len(piles)//3:
                max+=piles[i]
            count+=1
        return max
maxCoins([9,8,7,6,5,1,2,3,4])