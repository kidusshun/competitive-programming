class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for j in range(len(nums)+1):
            if j not in nums:
                return j