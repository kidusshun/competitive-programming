class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        odd = [0] * len(graph)

        def bfs(i):
            if odd[i]:
                return True
            
            q = deque([i])
            odd[i] = -1

            while q:
                i = q.popleft()
                for neigh in graph[i]:
                    if odd[i] == odd[neigh]:
                        return False
                    elif not odd[neigh]:
                        q.append(neigh)
                        odd[neigh] = -1 * odd[i]
            return True

        for i in range(len(graph)):
            if not bfs(i):
                return False
        
        return True