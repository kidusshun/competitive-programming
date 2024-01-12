class Solution:
    def balancedString(self, s: str) -> int:
        length = len(s)
        count = Counter(s)
        n = length//4
        extra = {}
        for key, val in count.items():
            if val>n:
                extra[key] = val - n
        
        if not extra:return 0

        ans = length
        i = 0
        for j in range(length):
            if s[j] in extra:
                extra[s[j]] -=1
            while max(extra.values()) <= 0:
                ans = min(ans, j-i+1)
                if s[i] in extra:
                    extra[s[i]] +=1
                i+=1
        return ans
