class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        result=0
        prefix_sum=0
        dict={0:1}
        for num in nums:
            prefix_sum += num
            if prefix_sum-goal in dict:
                result = result + dict[prefix_sum-goal]
            dict[prefix_sum] = dict.get(prefix_sum,0)+1
        return result