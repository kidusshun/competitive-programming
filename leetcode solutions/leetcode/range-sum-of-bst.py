# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        def traverse(root):
            nonlocal ans
            if root:
                if low<=root.val<=high:
                    ans+=root.val
                # elif root.val>high:
                #     return
                traverse(root.left)
                traverse(root.right)
        traverse(root)
        return ans