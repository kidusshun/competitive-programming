class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer1=0
        pointer2=1
        while pointer2<len(nums):
            if nums[pointer1] == 0 and nums[pointer2]!=0:
                nums[pointer1], nums[pointer2] = nums[pointer2], nums[pointer1]
                pointer1+=1
                pointer2+=1
            elif nums[pointer1] == 0 and nums[pointer2] == 0:
                pointer2+=1
            else:
                pointer1+=1
                pointer2+=1