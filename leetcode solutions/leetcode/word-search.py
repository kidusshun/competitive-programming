class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        moves = [[0,1],[0,-1],[1,0],[-1,0]]
        path = []
        self.possible = False
        seen = set()
        
        def backtrack(pos,ind):
            if ind>= len(word):
                self.possible = self.possible or "".join(path) == word
                if "".join(path) == word:
                    print(path)
                return
            for i in range(len(moves)):
                new_pos =[pos[0]+moves[i][0], pos[1]+moves[i][1]] 
                if 0<=new_pos[0]<len(board) and 0<=new_pos[1]<len(board[0]) and tuple(new_pos) not in seen:
                    if board[new_pos[0]][new_pos[1]] == word[ind]:
                        path.append(board[new_pos[0]][new_pos[1]])
                        seen.add(tuple(new_pos))
                        backtrack(new_pos,ind+1)
                        seen.discard(tuple(new_pos))
                        path.pop()
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    path.append(board[i][j])
                    seen.add(tuple([i,j]))
                    backtrack([i,j],1)
                    path.pop()
                    seen.discard(tuple([i,j]))
        return self.possible
        

