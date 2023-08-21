class Solution:
    def trusted(self, adj, i):
        for j, lst in adj.items():
            if i!=j and i not in lst:
                return False
        return True
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) == 0 and n == 1: return 1
        if len(trust) == 0: return -1
        adj = defaultdict(list)
        for i in range(1,n+1):
            adj[i] = []
        for lst in trust:
            adj[lst[0]].append(lst[1])
        
        for i in range(1,n+1):
            if adj[i] == [] and self.trusted(adj,i):
                return i
        return -1