class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = [0 for _ in range(n)]
        outgoing = [0 for _ in range(n)]

        for edge in trust:
            outgoing[edge[0] - 1] +=1
            incoming[edge[1] - 1] +=1
        town_judge = -1
        for i in range(n):
            if incoming[i] == n - 1 and outgoing[i] == 0:
                town_judge = i + 1
                break
        return town_judge