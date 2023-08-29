class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = deque([])
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]: return -1
        queue = deque([(0,0,1)])
        visited = set((0,0))
        direction = [(-1,0),(1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]

        while queue:
            l,r, length = queue.popleft()
            if l == r ==n-1:
                    return length
            for ro,c in direction:
                neigh_row = l + ro
                neigh_col = r+ c
                if 0<=neigh_row<n and 0 <= neigh_col <n and not grid[neigh_row][neigh_col]  and (neigh_row,neigh_col) not in visited:
                    visited.add((neigh_row,neigh_col))
                    queue.append((neigh_row,neigh_col,length + 1))
        return -1