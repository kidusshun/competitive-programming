class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        biggest = nums[0]
        ans = 0
        for i in range(1, len(nums)):
            if nums[i] < biggest:
                ans += i
                biggest = nums[i]
        return ans