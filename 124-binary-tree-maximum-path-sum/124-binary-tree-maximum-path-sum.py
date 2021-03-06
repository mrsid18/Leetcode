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
            
            left = dfs(node.left)
            right = dfs(node.right)
            self.res = max(self.res, node.val+left+right)
            
            return max(node.val+left, node.val+right, 0)
        
        dfs(root)
        return self.res