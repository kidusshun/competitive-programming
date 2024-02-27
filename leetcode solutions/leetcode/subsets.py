class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        path = []
        seen = set()
        
        def backtrack(ind):
            print(path)
            if ind > len(nums):
                return

            for i in range(ind+1,len(nums)):
                path.append(nums[i])
                if tuple(path) not in seen:
                    seen.add(tuple(path))
                    ans.append(path[:])
                    backtrack(i)
                path.pop()
        backtrack(-1)
        return ans