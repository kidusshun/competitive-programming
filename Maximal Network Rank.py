from collections import defaultdict
class Solution:
    def maximalNetworkRank(self, n: int, roads):
        adj = defaultdict(list)
        for edge in roads:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        res = 0
        for c1, c2 in itertools.combinations(adj.keys(),2):
            has = 1 if c1 in adj[c2] else 0
            res = max(res,len(graph[c1]) + len(graph[c2] - has))        
        return ans - 1



s = Solution()
s.maximalNetworkRank(4, [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]])