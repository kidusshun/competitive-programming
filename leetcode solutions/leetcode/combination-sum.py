class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.curr_sum = 0
        path = []
        ans = []
        seen = set()
        def backtrack():
            if self.curr_sum == target and tuple(sorted(path)) not in seen:
                seen.add(tuple(sorted(path)))
                ans.append(path[:])
                return
            elif self.curr_sum > target:
                return
            
            for i in range(len(candidates)):
                path.append(candidates[i])
                self.curr_sum +=candidates[i]
                backtrack()
                path.pop()
                self.curr_sum -=candidates[i]
        backtrack()
        return ans
