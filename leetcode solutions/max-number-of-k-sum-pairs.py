class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums)-1
        count = 0
        while left<right:
            curr = nums[left]+nums[right]
            if curr == k:
                count+=1
                left+=1
                right-=1
            elif curr > k:
                right-=1
            else:
                left+=1
        return count