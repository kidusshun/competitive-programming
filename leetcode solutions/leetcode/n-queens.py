class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        matrix = [["."]*n for _ in range(n) ]
        ans = []
        seen_row = set()
        seen_column = set()
        seen_primary = set()
        seen_secondary = set()
        self.count = 0
        def backtrack(pos):
            if self.count == n:
                ans.append(["".join(lst) for lst in matrix])
                return
            
            i = pos+1
            for j in range(n):
                if i not in seen_row and j not in seen_column and i+j not in seen_secondary and j-i not in seen_primary:
                    matrix[i][j] = "Q"
                    self.count+=1
                    
                    seen_row.add(i)
                    seen_column.add(j)
                    seen_primary.add(j-i)
                    seen_secondary.add(i+j)
                     
                    backtrack(i)
                    
                    seen_row.discard(i)
                    seen_column.discard(j)
                    seen_primary.discard(j-i)
                    seen_secondary.discard(i+j)

                    matrix[i][j] = "."
                    self.count -=1
        backtrack(-1)
        return ans