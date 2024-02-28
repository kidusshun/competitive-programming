# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(list)
        q = deque()
        q.append((root,(0,0)))
        self.left,self.right = 0,0
        
        def traverse():
            if not q:
                return
            
            curr,pos = q.popleft()
            
            self.left = min(self.left,pos[1])
            self.right = max(self.right,pos[1])
            
            d[pos].append(curr.val)
            d[pos].sort()

            if curr.left:
                q.append((curr.left,(pos[0]+1,pos[1]-1)))
            
            if curr.right:
                q.append((curr.right,(pos[0]+1,pos[1]+1)))

            traverse()
        
        
        traverse()

        ans = [[] for _ in range(self.right-self.left+1)]
        for key in d:
            pre = ans[key[1]-self.left]
            new = pre + d[key]
            ans[key[1]-self.left] = new

        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # left = 0
        # right = 0
        # def traverse(root,pos):
        #     nonlocal left
        #     nonlocal right
        #     if root:
        #         left = min(left,pos[1])
        #         right = max(right,pos[1])
        #         d[pos].append(root.val)
        #         d[pos].sort()
        #         traverse(root.left,(pos[0]+1,pos[1]-1))
        #         traverse(root.right,(pos[0]+1,pos[1]+1))
            
        # traverse(root,(0,0))
        # return ans