class Solution:
    def numPairsDivisibleBy60(self, time: list[int]) -> int:
        i, j = 0, 1
        ans = 0
        while j < len(time):
            if (time[i] + time[j])%60 == 0:
                ans += 1
            while j-i > 1:
                i += 1
                if (time[i] + time[j])%60 == 0:
                    ans += 1
            j += 1
        return ans
s = Solution()
s.numPairsDivisibleBy60([30,20,150,100,40])