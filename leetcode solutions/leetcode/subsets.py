class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        seen = set()
        
        def backtrack(ind):
            ans.append(path[:])
            if ind > len(nums):
                return

            for i in range(ind+1,len(nums)):
                path.append(nums[i])
                backtrack(i)
                path.pop()
        backtrack(-1)
        return ans