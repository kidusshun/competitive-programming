# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        if root:
            stack = [(root,float('-inf'))]

        while stack:
            curr, maximum = stack.pop()
            if curr.val >= maximum:
                ans += 1
                maximum = curr.val
            if curr.left:
                stack.append((curr.left, maximum))
            if curr.right:
                stack.append((curr.right,maximum))
        return ans