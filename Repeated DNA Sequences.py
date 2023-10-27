class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sub = s[:10]
        j= 10
        hash =defaultdict(int)
        hash[sub]+=1

        while j< len(s):
            sub = sub[1:] + s[j]
            hash[sub] +=1
            j+=1
        
        ans = []
        for sub, num in hash.items():
            if num> 1: ans.append(sub)
        return ans