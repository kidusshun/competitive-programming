class Solution:
    def videoStitching(self, clips: list[list[int]], time: int) -> int:
        dp = [float('inf')] * (T + 1)
        dp[0] = 0
        for i in range(1, T + 1):
            for start, end in clips:
                if start <= i <= end:
                    dp[i] = min(dp[start] + 1, dp[i])
        if dp[T] == float('inf'):
            return -1
        return dp[T]

Next
clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]]
s.videoStitching(clips, 10)

import heapq
heapq.heappop(heap)