class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n,m = len(image),len(image[0])
        stack = [(sr,sc)]
        start_col = image[sr][sc]
        visited = set((sr,sc))
        while stack:
            row,col = stack.pop(0)
            if image[row][col] == start_col:
                image[row][col] = color
            else: continue
            if row-1>=0 and (row-1,col) not in visited: 
                stack.append((row-1,col))
                visited.add((row-1,col))
            if row+1<n and (row+1,col) not in visited: 
                stack.append((row+1,col))
                visited.add((row+1,col))
            if col-1>=0 and (row,col-1) not in visited: 
                stack.append((row,col-1))
                visited.add((row,col-1))
            if col+1<m and (row,col+1) not in visited: 
                stack.append((row,col+1))
                visited.add((row,col+1))
        return image