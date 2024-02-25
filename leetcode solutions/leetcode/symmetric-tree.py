# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def traverse(l_tree,r_tree):
            if l_tree and r_tree:
                print(l_tree.val, r_tree.val)
                return l_tree.val == r_tree.val and traverse(l_tree.left,r_tree.right) and traverse(l_tree.right,r_tree.left)
            else:
                return l_tree == r_tree
        return traverse(root.left,root.right)