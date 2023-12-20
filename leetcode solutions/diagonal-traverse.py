class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        def isInbound(cell):
            return 0<=cell[0]<len(mat) and 0<=cell[1]<len(mat[0])
        ans = []
        up = True
        curr = (0,0)
        for i in range(len(mat)+len(mat[0])):
            while isInbound(curr):
                ans.append(mat[curr[0]][curr[1]])
                if up:
                    curr = (curr[0]-1,curr[1]+1)
                else:
                    curr = (curr[0]+1,curr[1]-1)
            if up and curr[1]<len(mat[0]):
                curr = (curr[0]+1,curr[1])
                up = False
            elif up:
                curr = (curr[0]+2, curr[1]-1)
                up = False
            elif not up and curr[0]>=len(mat):
                curr = (curr[0]-1,curr[1]+2)
                up = True
            else:
                curr = (curr[0],curr[1]+1)
                up = True
        return ans