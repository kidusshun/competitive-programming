class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        stack = []
        n = len(graph) - 1
        stack.append((0,[0]))
        while stack:
            curr = stack.pop()
            if curr[1] and curr[1][-1] == n:
                ans.append(curr[1])
            children = graph[curr[0]]
            for child in children:
                lst = curr[1].copy()
                lst.append(child)
                stack.append((child, lst))
        return ans