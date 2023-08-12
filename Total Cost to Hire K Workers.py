class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        ans = 0
        if candidates * 2 <= len(costs):
            right = costs[-candidates:]
            j = len(costs) - candidates - 1
            left = costs[:candidates]
            heapq.heapify(left)
            heapq.heapify(right)
            i = candidates

            while i<=j and k:
                if left[0]<=right[0]:
                    ans+=heapq.heappop(left)
                    heapq.heappush(left, costs[i])
                    i+=1
                else:
                    ans+=heapq.heappop(right)
                    heapq.heappush(right, costs[j])
                    j-=1
                k-=1
            left = left + right
            heapq.heapify(left)
            for _ in range(k):
                ans += heapq.heappop(left)
        else:
            heapq.heapify(costs)
            for _ in range(k):
                ans += heapq.heappop(costs)
        return ans 