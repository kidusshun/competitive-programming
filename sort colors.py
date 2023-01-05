class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1,len(nums)):
            if i==1:
                if nums[i]<nums[i-1]:
                    nums[i],nums[i-1]=nums[i-1],nums[i]
                continue
            smallest=nums[i]
            for j in range(i-1,-1,-1):
                if smallest <nums[j]:
                    nums[j+1],nums[j]=nums[j],nums[j+1]
                    smallest=nums[j]
                else:
                    break