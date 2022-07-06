# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = None
        
        def dfs(node):
            if not node: return False
            
            mid = node==p or node==q
            
            l = dfs(node.left)
            r = dfs(node.right)
            
            if mid+l+r>=2:
                self.res = node
            
            return mid or l or r
        dfs(root)
        return self.res
    
            
            
            
            
            
            
                