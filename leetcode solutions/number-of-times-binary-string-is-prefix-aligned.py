class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        max_ = 0
        count = 0
        for i, ind in enumerate(flips):
            max_ = max(max_, ind)
            if max_ == i+1:
                count+=1
        return count