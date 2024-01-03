class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        i,j = 0,0
        seen = set()
        while j<len(nums):
            if nums[i] not in seen:
                seen.add(nums[i])
                i+=1
                j+=1
            else:
                while j<len(nums) and nums[j] in seen:
                    j+=1
                if j<len(nums):
                    nums[i],nums[j] = nums[j],nums[i]
        return i