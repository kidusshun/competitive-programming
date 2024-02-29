class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        composition = ["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        ans = []
        path = []
        def backtrack(ind):
            if len(path)==len(digits):
                ans.append("".join(path))
                return
            
            for i in range(len(composition[int(digits[ind])-2])):
                path.append(composition[int(digits[ind])-2][i])
                backtrack(ind+1)
                path.pop()
        backtrack(0)
        return ans