class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d = defaultdict(int)
        l,r = 0,0
        ans = 0
        count = 0
        seen = set()
        while r<len(fruits):
            d[fruits[r]]+=1
            seen.add(fruits[r])
            while len(seen)>2:
                d[fruits[l]] -= 1
                if d[fruits[l]] == 0:
                    seen.discard(fruits[l])
                l+=1
            ans = max(r-l+1, ans)
            r+=1
        return ans