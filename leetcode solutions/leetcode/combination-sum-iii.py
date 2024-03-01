class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.curr_sum = 0
        ans = []
        path = []
        def backtrack(ind):
            print(path)
            if self.curr_sum ==n and len(path) == k:
                ans.append(path[:])
                return 
            elif self.curr_sum >n or len(path)>k:
                return
            

            for i in range(ind,10):
                path.append(i)
                self.curr_sum +=i
                backtrack(i+1)
                path.pop()
                self.curr_sum -=i
        
        backtrack(1)
        return ans