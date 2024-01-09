class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i= 0
        summ_ = 0
        length = float("inf")
        for j in range(len(nums)):
            summ_+=nums[j]
            while summ_>=target:
                length = min(length,j-i+1)
                summ_-=nums[i]
                i+=1
        if length == float("inf"):
            return 0
        return length
            