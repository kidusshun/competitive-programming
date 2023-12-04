class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        lst = []
        ghosts.append([0,0])
        for x,y in ghosts:
            x_diff,y_diff = x-target[0], y-target[1]
            lst.append(abs(x_diff)+abs(y_diff))
        return lst[-1] < min(lst[:-1])