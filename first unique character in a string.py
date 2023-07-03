class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans=[]
        duplicates = set()
        for i in s:
            if i not in ans and i in duplicates:
                ans.append(i)
            elif i in ans or i in duplicates:
                duplicates.add(i)
                ans.remove(i)
        if len(ans) == 0: return -1
        return s.index(ans[0])
s = Solution()
s.firstUniqChar('aadadaad')