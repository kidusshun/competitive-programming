class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        prev = points[0]
        ans = 0
        for x,y in points[1:]:
            x_diff,y_diff = x-prev[0], y-prev[1]
            if x_diff == y_diff:
                ans += abs(x_diff)
            elif x_diff!=0 and y_diff!=0:
                if abs(x_diff) < abs(y_diff):
                    ans += abs(y_diff)
                else:
                    ans += abs(x_diff)
            else:
                if x_diff == 0:
                    ans+=abs(y_diff)
                else:
                    ans+=abs(x_diff)
            prev = [x,y]
        return ans
            