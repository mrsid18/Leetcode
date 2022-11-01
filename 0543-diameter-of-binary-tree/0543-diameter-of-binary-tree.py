# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = -inf
        
        def dfs(node):
            if not node: return 0
            
            l = dfs(node.left)
            r = dfs(node.right)
            
            self.res = max(0, l+r, self.res)
            
            return 1+max(l, r)
        
        dfs(root)
        return self.res