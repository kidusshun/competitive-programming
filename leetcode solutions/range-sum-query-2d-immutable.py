class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.pref_matrix = []
        for row in matrix:
            pref = [row[0]]
            for i in range(1,len(row)):
                pref.append(pref[-1]+row[i])
            self.pref_matrix.append(pref)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for i in range(row1,row2+1):
            if col1 !=0:
                ans += self.pref_matrix[i][col2] - self.pref_matrix[i][col1-1]
            else:
                ans += self.pref_matrix[i][col2]
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)