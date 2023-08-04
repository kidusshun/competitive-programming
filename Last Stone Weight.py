class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(neg, stones))
        heapq.heapify(stones)

        while len(stones)>1:
            heapq.heappush(stones,heapq.heappop(stones) - heapq.heappop(stones))
        
        return -1* stones[0]