class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        ans = 0
        for lst in grid:
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
            ans += len(lst) -mid
        return ans

s = Solution()
s.countNegatives([[3,2],[1,0]])