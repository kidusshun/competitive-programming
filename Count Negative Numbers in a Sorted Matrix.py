class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        for row in grid:
            length = len(row)
            i,j = 0, length - 1

            while i<=j:
                mid = (i+j)//2
                if row[mid] >= 0:
                    i=mid+1
                else:
                    j= mid -1
            ans += length - i
        return ans