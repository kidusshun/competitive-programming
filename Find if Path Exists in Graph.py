class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        stack = [source]
        visited = set() 
        while stack:
            curr = stack.pop()
            if curr == destination: return True
            for child in adj[curr]:
                if child not in visited:
                    visited.add(child)
                    stack.append(child)
        return False

