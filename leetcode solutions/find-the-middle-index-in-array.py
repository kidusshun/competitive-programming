class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        summ_ = sum(nums)
        left = 0
        for i in range(len(nums)):
            comparator = (summ_ - nums[i] -left)
            if left == comparator:
                return i
            left += nums[i]
        return -1