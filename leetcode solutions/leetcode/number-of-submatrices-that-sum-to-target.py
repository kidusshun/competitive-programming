class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        pref = [[0]*(cols+1) for _ in range(rows+1)]
        ans = 0
        for i in range(rows):
            for j in range(cols):
                pref[i+1][j+1] = matrix[i][j] + pref[i][j+1] + pref[i+1][j] - pref[i][j]

        for r1 in range(1,rows+1):
            for r2 in range(r1,rows+1):
                d = {0:1}

                for col in range(1,cols+1):
                    curr = pref[r2][col] - pref[r1-1][col]
                    ans += d.get(curr -target,0)
                    d[curr] = d.get(curr,0) + 1
        
        print(pref)     
        return ans