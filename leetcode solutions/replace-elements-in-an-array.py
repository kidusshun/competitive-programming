class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        d = {num:ind for ind, num in enumerate(nums)}
        ans = nums.copy()
        for key,val in operations:
            ans[d[key]] = val
            d[val] = d[key]
        return ans