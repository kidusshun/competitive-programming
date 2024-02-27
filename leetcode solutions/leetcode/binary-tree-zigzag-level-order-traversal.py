# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lst = []
        def traverse(root,level):
            if root:
                if len(lst)<=level:
                    lst.append([root.val])
                else:
                    lst[level].append(root.val)
                traverse(root.left,level+1)
                traverse(root.right,level+1)
        traverse(root,0)
        for i in range(len(lst)):
            if i%2!=0:
                lst[i] = reversed(lst[i])
        print(lst)
        return lst