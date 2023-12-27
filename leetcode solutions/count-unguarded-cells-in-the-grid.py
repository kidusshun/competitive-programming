class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        mat = [[0]*n for _ in range(m)]
        for cell in walls:
            mat[cell[0]][cell[1]] = 'W'
        for cell in guards:
            mat[cell[0]][cell[1]] = 'G'
        
        def traverse(cell):
            i = cell[0]
            j = cell[1]
            mat[i][j] = 'G'
            j+=1
            count = 0
            while j<n and (mat[i][j] == 0 or mat[i][j]=='R'):
                if mat[i][j] !='R':
                    count+=1
                    mat[i][j] = 'R'
                j+=1
            i = cell[0]+1
            j = cell[1]
            while i<m and (mat[i][j] == 0 or mat[i][j]=='R'):
                if mat[i][j] !='R':
                    count+=1
                    mat[i][j] = 'R'
                i+=1
            i = cell[0]-1
            j = cell[1]
            while i>=0 and (mat[i][j] == 0 or mat[i][j]=='R'):
                if mat[i][j] !='R':
                    count+=1
                    mat[i][j] = 'R'
                i-=1
            i = cell[0]
            j = cell[1]-1
            while j>=0 and (mat[i][j] == 0 or mat[i][j]=='R'):
                if mat[i][j] !='R':
                    count+=1
                    mat[i][j] = 'R'
                j-=1
            return count


        reds = 0        
        for guard in guards:
            reds += traverse(guard)
        return m*n -(reds+len(guards)+len(walls))