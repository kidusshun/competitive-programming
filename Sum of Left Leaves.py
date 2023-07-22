# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isleaf(self, node:TreeNode) -> bool:
        return not node.left and not node.right
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0
        stack = []
        if root:
            stack.append(root)
        
        while stack:
            curr = stack.pop()
            if curr.left:
                stack.append(curr.left)
                if self.isleaf(curr.left):
                    ans += curr.left.val
            if curr.right:
                stack.append(curr.right)
        return ans