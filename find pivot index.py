class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        sum_left=0
        for ind in range(len(nums)):
            if sum_left== (total-sum_left-nums[ind]):
                return ind
            sum_left+=nums[ind]
        return -1
        