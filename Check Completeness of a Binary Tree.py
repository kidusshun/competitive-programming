# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isleafNode(self, node):
        return not node.left and not node.right
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append(root)
        isNull = False

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if not curr:
                    isNull = True
                else:
                    if isNull: return False
                    queue.append(curr.left)
                    queue.append(curr.right)
        
        return True