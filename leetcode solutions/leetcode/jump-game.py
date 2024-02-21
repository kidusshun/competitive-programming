class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_ind = 0
        for i, num in enumerate(nums):
            print(i,max_ind)
            if max_ind >= i:
                reached_ind = num+i
                max_ind = max(max_ind, reached_ind)
        if max_ind >= len(nums)-1:
            return True
        return False
