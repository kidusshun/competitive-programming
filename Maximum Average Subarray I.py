class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxim = sum(nums[:k])
        sub = maxim
        for i in range(len(nums)-k):
            sub = sub -nums[i] + nums[k+i]
            if sub> maxim :
                maxim = sub
        return maxim/k
            