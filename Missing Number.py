class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] !=1:
                return nums[i] + 1

s = Solution()
s.missingNumber([3,0,1])