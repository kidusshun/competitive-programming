class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans = 0
        count = [0] * 60
        for num in range(len(time)):
            index = time[num] % 60
            ans += count[(60 - index)%60]
            count[index] += 1
        return ans