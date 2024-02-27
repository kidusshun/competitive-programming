# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.max_dif = 0
        def traverse(root,max_,min_):
            if root:
                self.max_dif = max(abs(root.val-max_),self.max_dif, abs(root.val - min_))
                if root.val > max_:
                    max_ = root.val
                elif root.val < min_:
                    min_ = root.val
                traverse(root.left,max_,min_)
                traverse(root.right,max_,min_)
        traverse(root,root.val,root.val)
        return self.max_dif