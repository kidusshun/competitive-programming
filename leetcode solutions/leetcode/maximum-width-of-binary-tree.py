# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d_min = defaultdict(lambda: float("inf"))
        d_max = defaultdict(lambda: float("-inf"))
        self.max_ = 0

        def traverse(root,pos,level):
            if root:
                d_min[level] = min(d_min[level],pos)
                d_max[level] = max(d_max[level],pos)
                print(root.val,pos,level,d_min[level],d_max[level])
                self.max_ = max(self.max_, d_max[level] - d_min[level])
                traverse(root.left,pos*2,level+1)
                traverse(root.right,pos*2+1,level+1)
        
        traverse(root,1,0)
        return self.max_+1