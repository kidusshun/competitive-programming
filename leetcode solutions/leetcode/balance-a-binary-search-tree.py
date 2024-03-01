# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        lst = []
        def inorder(root):
            if root:
                inorder(root.left)
                lst.append(root.val)
                inorder(root.right)
            
        inorder(root)
        
        def balance(lst):
            if lst:
                center = len(lst)//2
                root = TreeNode(lst[center])
                root.left = balance(lst[:center])
                root.right = balance(lst[center+1:])
                return root
            else:
                return None
        return balance(lst)