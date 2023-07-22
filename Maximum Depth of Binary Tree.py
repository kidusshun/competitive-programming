# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isleaf(self, node: TreeNode) -> bool:
        return not node.left and not node.right
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0
        stack = []
        if root:
            stack.append((root,1))
        while stack:
            curr_node, level = stack.pop()
            if self.isleaf(curr_node):
                ans = max(ans, level)
            else:
                if curr_node.left:
                    stack.append((curr_node.left, level + 1))
                if curr_node.right:
                    stack.append((curr_node.right,level + 1))
        return ans