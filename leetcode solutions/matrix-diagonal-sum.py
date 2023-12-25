class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        i,j = 0,0
        count = 0
        while i<len(mat) and j<len(mat):
            count+=mat[i][j]
            i+=1
            j+=1
        i,j = 0, len(mat)-1

        while i<len(mat) and j>=0:
            count+=mat[i][j]
            i+=1
            j-=1
        if len(mat)%2!=0:
            count -= mat[len(mat)//2][len(mat)//2]
        return count