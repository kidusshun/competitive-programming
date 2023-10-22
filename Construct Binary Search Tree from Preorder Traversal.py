# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstFromPreorder(self, preorder: list[int]) -> TreeNode:
        graph = TreeNode()
        graph.val=preorder[0]
        par = [graph]
        for i in preorder[1:]:
            node = TreeNode(val=i)
            curr = par.pop()
            if i< curr.val:
                curr.left = node
                par.append(curr)
                par.append(node)
            else:
                curr = par.pop()
                curr.right = node
        return graph
s = Solution()
s.bstFromPreorder([8,5,1,7,10,12])