from collections import Counter
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        ans = 0
        for i in range(len(startGene)):
            if startGene[i] != endGene[i]: ans+=1
        
        if endGene in startGene: return ans
        return -1

s = Solution()

s.minMutation("AACCGGTT","AACCGGTA",["AACCGGTA"])