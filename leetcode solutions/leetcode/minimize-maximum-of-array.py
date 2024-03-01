class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        cur_sum = nums[0]
        max_ = 0
        if nums.index(max(nums)) == 0:
            return nums[0]
        for i in range(1,len(nums)):
            cur_sum += nums[i]
            avg = math.ceil(cur_sum/(i+1))
            max_ = max(avg,max_)
        return max(max_,nums[0])