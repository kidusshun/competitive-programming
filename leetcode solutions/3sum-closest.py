class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        length = len(nums)
        summ_ = float("inf")
        for fixed in range(length):
            if fixed > 0 and nums[fixed] == nums[fixed-1]:
                continue
            i,j = fixed+1, length-1
            while i<j:
                curr_sum = nums[i]+nums[fixed]+nums[j]
                if abs(curr_sum - target) <= abs(summ_ - target):
                    summ_ = curr_sum
                    if summ_ == target:
                        return summ_
                if curr_sum <target:
                    i+=1
                elif curr_sum > target:
                    j-=1
        return summ_