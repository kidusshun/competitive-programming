# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverse(root,ans):
            if root:
                ans.append(root.val)
                if root.left:
                    traverse(root.left, ans)
                else:
                    ans.append(None)
                if root.right:
                    traverse(root.right, ans)
                else:
                    ans.append(None)
        q_ans = []
        p_ans = []
        traverse(q,q_ans)
        traverse(p,p_ans)
        print(q_ans)
        print(p_ans)
        return q_ans == p_ans