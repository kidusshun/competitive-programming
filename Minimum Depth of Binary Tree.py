# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isleaf(node):
        return not node.left and not node.right
    def minDepth(self, root: TreeNode) -> int:
        queue = deque()
        queue.append((root,1))
        while queue:
            length = len(queue)
            for _ in range(length):
                curr, path = queue.popleft()
                if self.isleaf(curr):
                    return path
                queue.append((curr.left, path+1))
                queue.append((curr.right, path+1))

root = TreeNode(3)
l = TreeNode(9)
r = TreeNode(30)
root.left = l
root.right = r
m = TreeNode(15)
p = TreeNode(7)
r.left = m
r.right = p

s = Solution()
s.minDepth(root)