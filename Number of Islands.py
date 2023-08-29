class Solution:
    def inBound(self, row: int, col: int, grid: list[list[int]]) -> bool:

        if row < 0 or row >= len(grid):
            return False

        if col < 0 or col >= len(grid[0]):
            return False

        return True

    def getNeighbors(self, row: int, col: int, grid: list[list[str]]):

        nbrs = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for x, y in directions:
            new_row, new_col = row+x, col+y
            if self.inBound(new_row, new_col, grid) and grid[row][col] == grid[new_row][new_col]:
                nbrs.append((new_row, new_col))

        return nbrs

    def traverse(self, row, col,visited,gird,ans):
        stack = [(row,col)]
        while stack:
            row,col = stack.pop()
            for neigh_row,neigh_col in self.getNeighbors(row,col,grid):
                if grid[neigh_row][neigh_col] == '1' and (neigh_row,neigh_col) not in visited:
                    visited.append((neigh_row,neigh_col))
                    stack.append((neigh_row,neigh_col))
        ans += 1
        return ans


    def numIslands(self, grid: list[list[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = []
        ans = 0

        for row in range(rows):
            for col in range(cols):
                if (row,col) not in visited and grid[row][col] == '1':
                    visited.append((row,col))
                    ans = self.traverse(row,col,visited,grid, ans)
        
        return ans

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
s = Solution()
print(s.numIslands(grid))