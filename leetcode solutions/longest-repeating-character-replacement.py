class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = set()
        d = defaultdict(int)
        l = 0
        ans =0
        frequent = 0
        for r in range(len(s)):
            d[s[r]]+=1
            frequent = max(frequent, d[s[r]])
            while r-l+1 - frequent >k:
                d[s[l]] -=1
                l+=1

            ans = max(ans, r-l+1)
        return ans