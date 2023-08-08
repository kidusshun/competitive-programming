class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        for i,row in enumerate(mat):
            ones = row.count(1)
            heappush(heap,(ones,i))
        ans = []
        for i in range(k):
            num,i = heappop(heap)
            ans.append(i)
        
        return ans