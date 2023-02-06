class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        new=dict()
        for i in range(len(nums)):
            if nums[i] not in new:
                new[nums[i]]=0