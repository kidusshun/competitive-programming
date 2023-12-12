class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        nums = list(set(nums))
        nums.sort()
        i = 0
        maxim = 1
        for j in range(1,len(nums)):
            if nums[j]-1 == nums[j-1]:
                maxim = max(maxim,j-i+1)
            else:
                i = j
        return maxim