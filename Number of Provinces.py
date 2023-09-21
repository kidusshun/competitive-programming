class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(isConnected)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)

        ans = 1
        
        nodes = set(list(graph.keys()))
        print(nodes)
        stack = [nodes.pop()]

        while stack or nodes:
            if stack: curr = stack.pop()
            else: 
                curr = nodes.pop()
                ans += 1

            for node in graph[curr]:
                if node in nodes:
                    nodes.remove(node)
                    stack.append(node)
            
        return ans