class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        length = len(grid)
        ans = 0
        for i, lst in enumerate(grid):
            l,r = 0, len(lst)-1

            while l<=r:
                mid = l + (r-l)//2
                if lst[mid] > 0:
                    l=mid + 1
                elif lst[mid] < 0:
                    r= mid - 1
                else:
                    ans += len(lst)-mid-1
                    break
            ans += (len(lst) -mid) * (length -i)
        return ans

s = Solution()
s.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])