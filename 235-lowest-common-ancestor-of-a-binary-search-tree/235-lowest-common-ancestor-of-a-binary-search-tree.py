# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        tp = p if p.val>q.val else q
        tq = p if p.val<q.val else q
        
        def dfs(node):
            if not node:
                return 
            
            if tq.val<=node.val<=tp.val:
                print(node.val)
                return node
            
            if node.val>tq.val:
                return dfs(node.left)
            else:
                return dfs(node.right)
        
        return dfs(root)