class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = []
        ans = []

        def backtrack(op,cl):
            if op<cl or op> n or cl >n:
                return
            if len(path) == 2*n:
                ans.append("".join(path))
                return 
            
            path.append("(")
            backtrack(op+1,cl)
            path.pop()
            path.append(")")
            backtrack(op,cl+1)
            path.pop()
        backtrack(0,0)
        return ans