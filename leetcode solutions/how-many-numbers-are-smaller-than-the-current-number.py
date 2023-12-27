class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        lst=[0]*len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]>nums[j] and i!=j:
                    lst[i]+=1
        return lst
             

        
