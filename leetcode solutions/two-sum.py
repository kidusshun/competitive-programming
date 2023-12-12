class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d=defaultdict(int)
        for i,num in enumerate(nums):
            d[num] = i
        
        for i in range(len(nums)):
            t = target - nums[i]
            if d[t] and i!=d[t]:
                return [i,d[t]]
