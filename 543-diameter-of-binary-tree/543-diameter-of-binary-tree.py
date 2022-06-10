# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        cache = {None: -1}
        self.dia = -inf
        def dfs(node):
            if node in cache:
                return cache[node]
            l = dfs(node.left)
            r = dfs(node.right)
            cache[node] = max(l+1, r+1)
            self.dia = max(self.dia, 2+l+r)
            return cache[node]
        
        dfs(root)
        return self.dia
            
            
            
            
            
            
            
          