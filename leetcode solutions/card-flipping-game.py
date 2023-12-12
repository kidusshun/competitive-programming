class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        doubles = set()
        for front, back in zip(fronts,backs):
            if front == back:
                doubles.add(front)
        ans = float("inf")
        for num in fronts+backs:
            if num not in doubles:
                ans = min(ans, num)
        if ans == float("inf"):
            return 0
        return ans