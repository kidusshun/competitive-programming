class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        self.curr_sum = 0
        ans = []
        
        candidates.sort()
        seen = set()
        
        def backtrack(ind):
            if self.curr_sum == target:
                ans.append(path[:])
                return
            
            if self.curr_sum > target:
                return
            
            for i in range(ind, len(candidates)):
                if i> ind and candidates[i]==candidates[i-1]:
                    continue
                else:
                    path.append(candidates[i])
                    self.curr_sum += candidates[i]
                    backtrack(i+1)
                    path.pop()
                    self.curr_sum -= candidates[i]
            
        backtrack(0)
        return ans