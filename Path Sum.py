# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def traverse(node,summ):
            if not node:
                return
            summ += node.val

            if node.left or node.right:
                return traverse(node.left, summ) or traverse(node.right, summ)
            else:
                return targetSum == summ
        return traverse(root,0)