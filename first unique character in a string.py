class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans=[]
        duplicates = set()
        for i,char in enumerate(s):
            if char not in ans and char not in duplicates:
                ans.append(char)
            elif char in ans:
                duplicates.add(char)
                ans.remove(char)
        if len(ans) == 0: return -1
        return s.index(ans[0][0])