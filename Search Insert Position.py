class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,r = 0,n-1
        while l<=r:
            mid = l + (r-l)//1
            if nums[mid] > target:
                r=mid-1
            elif nums[mid] < target:
                l=mid+1
            else:
                return mid
        if nums[mid]<target:
            return mid+1
        elif nums[mid]> target and mid ==0:
            return 0
        else: return mid-1