from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list[list[int]]:
        ans = []
        queue = deque()
        state = 'left'
        if root:
            queue.append(root)
        
        while queue:
            if state == 'left':
                ans.append([node.val for node in queue])
            else:
                ans.append([node.val for node in reversed(queue)])

            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if state == 'left': state = 'right'
            else: state = 'left'
        
        return ans

root = TreeNode(3)
l = TreeNode(9)
r = TreeNode(20)
root.left = l
root.right = r
m= TreeNode(15)
s= TreeNode(7)

r.left = m
r.right = s

s = Solution()
s.zigzagLevelOrder(root)
