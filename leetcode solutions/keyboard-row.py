class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ["qwertyuiop","asdfghjkl","zxcvbnm"]
        ans = []
        for word in words:
            same = True
            prev = None
            for char in word:
                for i,row in enumerate(rows):
                    if char.lower() in row and prev == None:
                        prev = i
                    elif char.lower() in row:
                        if i != prev:
                            same = False
                            break
                if not same: break
            if same:
                ans.append(word)
        return ans
