from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_picked = 0
        basket = collections.defaultdict(int)
        ind1=0
        for ind2,val in enumerate(fruits):
            basket[val]+=1
            while len(basket) > 2:
                basket[fruits[ind1]] -= 1
                if basket[fruits[ind1]] == 0:
                    del basket[fruits[ind1]]
                ind1 += 1
            max_picked = max(max_picked, ind2 - ind1 + 1)
        return max_picked