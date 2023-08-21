from collections import defaultdict
class Solution:
    def dfs(self,adj, node,quiet):
        stack = [node]
        mini = quiet[node]
        ans_node = node
        while stack:
            curr = stack.pop()
            if mini > quiet[curr]:
                mini = quiet[curr]
                ans_node = curr
            for child in adj[curr]:
                stack.append(child)
        return ans_node
    def loudAndRich(self, richer: list[list[int]], quiet: list[int]) -> list[int]:
        adj = dict()
        for i in range(len(quiet)):
            adj[i] = []
        for edge in richer:
            adj[edge[1]].append(edge[0])
        ans = [0 for num in range(max(adj.keys()) + 1)]
        lst = adj.keys()
        for node in lst:
            ans[node] = self.dfs(adj.copy(), node, quiet)

        return ans

s = Solution()
print(s.loudAndRich([[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], [3,2,5,4,6,1,7,0]))