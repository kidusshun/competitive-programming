from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        ans = 0
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        queue = deque([(0,0)])
        visited[0][0] = True
        def find(row,col):
            counter = 0
            q = [[row,col]]
            while q:
                row, col = q.pop()
                neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
                for r, c in neighbors:
                    if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols and not visited[neighbor_row][neighbor_col] and grid[neighbor_row][neighbor_col] == 1:
                        q.append([r,c])
                        visited[r][c] = True
                        counter +=1
            return counter
        while queue:
            row, col = queue.popleft()

            if grid[row][col] == 1:
                val = find(row,col)
                ans = max(ans,val)

            neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
            for neighbor_row, neighbor_col in neighbors:
                if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols and not visited[neighbor_row][neighbor_col]:
                    queue.append((neighbor_row, neighbor_col))
                    visited[neighbor_row][neighbor_col] = True
        return ans

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]

s = Solution()
s.maxAreaOfIsland(grid)