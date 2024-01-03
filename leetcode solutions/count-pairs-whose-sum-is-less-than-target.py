class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        left, right= 0, len(nums)-1
        ans = 0
        while left<right:
            curr = nums[left]+nums[right]
            if curr<target:
                ans+=(right-left)
                left+=1
            else:
                right-=1
        return ans