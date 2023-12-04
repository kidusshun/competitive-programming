class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        lst = []
        for cand in candies:
            if cand+extraCandies >= maximum:
                lst.append(True)
            else:
                lst.append(False)
        return lst