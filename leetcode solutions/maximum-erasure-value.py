class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        i = 0
        curr_sum = 0
        max_sum = 0
        for j in range(len(nums)):
            while nums[j] in seen:
                seen.remove(nums[i])
                curr_sum -= nums[i]
                i+=1
            seen.add(nums[j])
            curr_sum += nums[j]
            max_sum = max(curr_sum, max_sum)
        return max_sum