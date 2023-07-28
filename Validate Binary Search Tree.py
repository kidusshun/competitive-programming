# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(root):
            if not root:
                return []
            return traverse(root.left) + [root.val] + traverse(root.right)
        traversed = traverse(root)
        return traversed == sorted(list(set(traversed)))