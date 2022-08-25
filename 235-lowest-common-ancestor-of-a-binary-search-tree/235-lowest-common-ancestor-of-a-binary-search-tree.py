# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return 
            
            if node.val>q.val and node.val>p.val:
                return dfs(node.left)
            elif node.val < q.val and node.val<p.val:
                return dfs(node.right)
            else: return node
        
        return dfs(root)
            