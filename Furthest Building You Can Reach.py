import heapq
class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        heap = []
        heapq.heapify(heap)
        for i in range(len(heights) - 1):
            dif = heights[i + 1] - heights[i]
             
            if dif > 0:
                heapq.heappush(heap, dif)
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)
            if bricks < 0:
                return i
        return len(heights) - 1

s = Solution()
s.furthestBuilding([4,2,7,6,9,14,12],5,1)