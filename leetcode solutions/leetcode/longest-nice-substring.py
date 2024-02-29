class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        def backtrack(word):
            unique = set(word)
            for i in range(len(word)):
                if word[i].swapcase() not in unique:
                    left = backtrack(word[:i])
                    right = backtrack(word[i+1:])
                    return max(left,right, key= len)
            return word

        return backtrack(s)