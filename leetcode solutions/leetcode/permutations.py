class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        seen_ind = set()
        def backtrack():
            
            if len(path) == len(nums):
                ans.append(path.copy())
                return
            
            for i in range(len(nums)):
                if i not in seen_ind:
                    seen_ind.add(i)
                    path.append(nums[i])
                    backtrack()
                    seen_ind.discard(i)
                    path.pop()
        backtrack()
        return ans