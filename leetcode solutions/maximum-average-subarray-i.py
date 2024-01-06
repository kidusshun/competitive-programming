class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ_ = sum(nums[:k])
        max_ = summ_/k
        i = 0
        for j in range(k, len(nums)):
            summ_ = summ_ - nums[i] + nums[j]
            max_ = max(max_, summ_/k)
            i+=1
        return max_
