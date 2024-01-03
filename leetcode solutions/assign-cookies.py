class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        j = 0
        i = 0
        count = 0
        
        while i< len(g) and j < len(s):
            if g[i]<= s[j]:
                j+=1
                i+=1
                count+=1
            else:
                j+=1
        return count