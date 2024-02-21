class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counts = Counter(s)
        i,j = 0,0
        seen = set()
        ans = []
        while j<len(s):
            seen.add(s[j])
            counts[s[j]]-=1
            if counts[s[j]] ==0:
                seen.remove(s[j])
                if len(seen) ==0:
                    ans.append(j-i+1)
                    i=j+1
            j+=1
        return ans