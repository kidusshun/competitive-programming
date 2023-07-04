class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        sub_sum=0
        size=float('inf')
        for j in range(len(nums)):
            sub_sum += nums[j]
            while i <= j and sub_sum>=target:
                if sub_sum >= target and (j-i+1)<size:
                    size=(j-i+1)
                sub_sum -=nums[i]
                i+=1
        
        if size == float('inf'): return 0
        return size