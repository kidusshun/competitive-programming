class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i,j = 0,len(nums)-1
        while i<=j:
            while i<=j and nums[i]!=val:
                i+=1
            if i<=j:
                nums[i], nums[j] = nums[j], nums[i]
                j-=1
        return i