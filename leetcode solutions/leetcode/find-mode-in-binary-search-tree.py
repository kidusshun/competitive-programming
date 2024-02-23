# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        d = defaultdict(int)
        def helper(root):
            if root:
                d[root.val] +=1
                helper(root.left)
                helper(root.right)
        helper(root)
        max_ = max(d.values())
        for key,val in d.items():
            if val == max_:
                lst.append(key)
        return lst