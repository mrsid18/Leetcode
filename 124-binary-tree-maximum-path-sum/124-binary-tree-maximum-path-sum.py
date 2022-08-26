# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -inf
        
        def dfs(node):
            if not node: return 0 
            
            l = dfs(node.left)
            r = dfs(node.right) 
            ans = max(l,r, 0)+node.val
            self.res = max(self.res, l+r+node.val, ans)
            
            return ans
        
        dfs(root)
        
        return self.res
        
        