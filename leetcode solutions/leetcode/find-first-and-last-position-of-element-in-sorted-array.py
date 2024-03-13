class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r = 0, len(nums) -1
        ans = [-1,-1]
        
        if len(nums) == 0:
            return ans
        
        while l <= r:
            mid = (l+r)//2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid -1
        
        if nums[l%len(nums)] == target:
            ans[0] = l
        
        l,r = 0, len(nums) -1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid +1
        
        if nums[r%len(nums)] == target:
            ans[1] = r
            
        return ans
