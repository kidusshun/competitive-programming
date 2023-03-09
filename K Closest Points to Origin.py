class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        lst=[]
        for (x,y) in points:
            dist=x**2 + y**2
            lst.append([dist,[x,y]])
        lst.sort()
        closest=[]
        for i in range(k):
            closest.append(lst[i][1])
        return closest