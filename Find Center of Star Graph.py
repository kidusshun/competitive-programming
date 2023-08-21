class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adj = defaultdict(int)
        for edge in edges:
            adj[edge[0]] +=1
            adj[edge[1]] +=1
        n = len(adj.keys())
        for node in adj.keys():
            if adj[node] == n - 1:
                return node