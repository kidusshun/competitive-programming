class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        @lru_cache(None)
        def dfs(node):
            if node not in graph:
                return node
            minimum = node
            for neighbour in graph[node]:
                candidate = dfs(neighbour)
                if quiet[minimum] > quiet[candidate]:
                    minimum = candidate 
            return minimum  
        n = len(quiet)
        graph = defaultdict(list)
        for u , v in richer:
            graph[v].append(u)
        return list(map(dfs , range(n)))