class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        max_ = 0
        for j in range(len(grid)-2):
            for i in range(len(grid[0])-2):
                sum_ = 0
                sum_+= sum(grid[j][i:i+3])
                sum_+= sum(grid[j+2][i:i+3])
                sum_+= grid[j+1][i+1]
                max_ = max(max_,sum_)
        return max_