# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = TreeNode(val)
        if not root:
            return node
        stack = [root]
        while stack:
            curr = stack.pop()
            if val < curr.val:
                if curr.left:
                    stack.append(curr.left)
                else:
                    curr.left = node
            else:
                if curr.right:
                    stack.append(curr.right)
                else:
                    curr.right = node
        return root