class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[0])
        intersection = points[0]
        arrows = 1
        print(points)
        for left, right in points[1:]:
            if intersection[0]<=left<=intersection[1]:
                intersection = [max(intersection[0],left), min(right,intersection[1])]
            else:
                arrows+=1
                intersection = [left,right]
        return arrows