# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) ==0:
            return None
        center = nums.index(max(nums))
        root = TreeNode(nums[center])
        root.left = self.constructMaximumBinaryTree(nums[:center])
        root.right = self.constructMaximumBinaryTree(nums[center+1:])
        return root