class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.pref = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i==0 and j==0:
                    self.pref[i][j] = matrix[i][j]
                elif i==0:
                    self.pref[i][j] = matrix[i][j]+ self.pref[i][j-1]
                elif j == 0:
                    self.pref[i][j] = matrix[i][j] +self.pref[i-1][j]
                else:
                    self.pref[i][j] = matrix[i][j] + self.pref[i-1][j] + self.pref[i][j-1] - self.pref[i-1][j-1]
        print(self.pref)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 !=0 and col1!=0:
            return self.pref[row2][col2] - self.pref[row2][col1-1] - self.pref[row1-1][col2] + self.pref[row1-1][col1-1]
        elif row1==0 and col1!=0:
            return self.pref[row2][col2] - self.pref[row2][col1-1]
        elif col1==0 and row1!=0:
            return self.pref[row2][col2] - self.pref[row1-1][col2]
        else:
            return self.pref[row2][col2]
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)