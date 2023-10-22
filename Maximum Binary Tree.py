# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        def rec(arr):
            if len(arr)==0: return None
            root = max(arr)
            graph = TreeNode()
            graph.val = root
            ind = arr.index(root)
            graph.left = rec(arr[:ind])
            graph.right = rec(arr[ind+1:])
            return graph
        return rec(nums)