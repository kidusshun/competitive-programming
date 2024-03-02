class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        smalls = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                smalls[(r//3,c//3)].add(board[r][c])
        
        def backtrack(r,c):
            if r==9:
                return True
            if c == 9:
                return backtrack(r+1,0)
            
            if board[r][c] == ".":
                for i in range(1,10):
                    if str(i) not in rows[r] and str(i) not in cols[c] and str(i) not in smalls[(r//3,c//3)]:
                        board[r][c] = str(i)
                        
                        rows[r].add(board[r][c])
                        cols[c].add(board[r][c])
                        smalls[(r//3,c//3)].add(board[r][c])
                        if backtrack(r,c+1):
                            return True
                        else:
                            rows[r].discard(board[r][c])
                            cols[c].discard(board[r][c])
                            smalls[(r//3,c//3)].discard(board[r][c])
                            board[r][c] = "."
                return False
            else:
                return backtrack(r,c+1)
            
        backtrack(0,0)