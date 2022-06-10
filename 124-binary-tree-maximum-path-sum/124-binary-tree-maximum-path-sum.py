# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxsum = -inf
        def dfs(node):
            if not node:
                return 0
            lmax = dfs(node.left)
            rmax= dfs(node.right)
            s = node.val + max(lmax, rmax,0)
            self.maxsum = max(self.maxsum, node.val+max(lmax,0)+max(rmax,0))
            
            return s
        
        dfs(root)
        return self.maxsum