class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        word = Counter(p)
        window = Counter(s[:len(p)-1])
        l = 0
        ans = []

        for r in range(len(p)-1,len(s)):
            window[s[r]] +=1
            if word == window:
                ans.append(l)
            
            window[s[l]] -= 1
            if not window[s[l]]:
                del window[s[l]]
            l+=1
        return ans