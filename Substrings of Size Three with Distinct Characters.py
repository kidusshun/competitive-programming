from collections import Counter

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        dit = Counter(s[:3])
        i,j =0,3
        if len(dit) == 3: ans =1
        else:ans = 0
        while j <len(s):
            dit[s[i]] -=1
            if dit[s[i]] == 0:
                del dit[s[i]]
            i+=1
            dit[s[j]] = dit.get(s[j],0)+1
            j+=1
            if len(dit) == 3:
                ans+=1
        return ans
s = Solution()
s.countGoodSubstrings("xyzzaz")