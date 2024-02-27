class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []
        def inorder(root):
            if root is None: return None
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
        inorder(root)
        return True if arr == sorted(list(set(arr))) else False