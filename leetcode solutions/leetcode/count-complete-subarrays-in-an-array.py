class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct_nums = len(set(nums))
        ans = 0        
        for i in range(len(nums)):
            seen = set()
            for j in range(i,len(nums)):
                seen.add(nums[j])
                if len(seen) == distinct_nums:
                    ans+=1
        return ans