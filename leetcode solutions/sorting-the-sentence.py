class Solution:
    def sortSentence(self, s: str) -> str:
        lst = [""]*len(s.split(" "))
        for word in s.split(" "):
            ind  = int(word[-1])
            lst[ind-1] = word[:-1]
        return " ".join(lst)