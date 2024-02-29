# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def backtrack(lst):
            if len(lst)>0:
                center = len(lst)//2
                root = TreeNode(lst[center])
                root.left = backtrack(lst[:center])
                root.right = backtrack(lst[center+1:])
                return root
            else:
                return None


        return backtrack(nums)