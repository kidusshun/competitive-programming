class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        word = "".join(garbage)
        characters = ["M","P","G"]
        ans = 0

        for c in characters:
            if c in word:
                prefix = 0
                for i in range(len(garbage)):
                    coun = garbage[i].count(c)
                    if coun !=0:
                        prefix = i
                    ans+=coun
                ans+=sum(travel[:prefix])
        return ans