# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        stack = []
        stack.append((root,f"{root.val}"))
        while stack:
            curr = stack.pop()
            left = curr[0].left
            right = curr[0].right
            if right:
                stack.append((right,curr[1] + f"->{right.val}"))
            if left:
                stack.append((left, curr[1] + f"->{left.val}"))
            if not right and not left:
                ans.append(curr[1])
        return ans
