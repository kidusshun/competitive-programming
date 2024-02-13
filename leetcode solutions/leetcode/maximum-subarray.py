class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pref = 0
        min_pref = 0
        max_sum = float("-inf")
        for num in nums:
            pref +=num
            if pref - min_pref >max_sum:
                max_sum = pref - min_pref
            if pref < min_pref:
                min_pref =pref
        return max_sum