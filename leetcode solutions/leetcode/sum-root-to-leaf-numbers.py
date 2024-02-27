# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def traverse(root,num):
            nonlocal ans
            
            if not root.left and not root.right:
                print(num)
                ans += int(str(num+str(root.val)))
            
            elif root.left and root.right:

                traverse(root.left,num+str(root.val))
                traverse(root.right,num+str(root.val))
            elif root.left:
                traverse(root.left,num+str(root.val))
            else:
                traverse(root.right,num+str(root.val))
        
        traverse(root, "")
        return ans