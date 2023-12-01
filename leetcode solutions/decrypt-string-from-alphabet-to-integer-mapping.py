class Solution:
    def freqAlphabets(self, s: str) -> str:
        word = ""
        i = len(s) - 1
        while i >=0:
            if s[i] =="#":
                cur = s[i-2] + s[i-1]
                word += chr(97 + int(cur)-1)
                i-=3
            else:
                word += chr(97 + int(s[i])-1)
                i-=1
        return word[::-1]
