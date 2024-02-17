class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row = defaultdict(int)
        column = defaultdict(int)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                row[i] = max(row[i],grid[i][j])
                column[j] = max(column[j],grid[i][j])
        print(row)
        print(column)
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans += min(row[i],column[j]) - grid[i][j]
        return ans