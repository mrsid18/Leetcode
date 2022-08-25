# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        def dfs(node):
            if not node: return 0
            
            res = 0
            
            if node==p or node==q: 
                res += 1
                
            res += dfs(node.left) + dfs(node.right)
            
            if res==2 and not self.ans:
                self.ans = node
            
            return res
        
        dfs(root)
        return self.ans
            
            