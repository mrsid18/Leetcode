# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #length of left side + max length of right side
        cache = {None: -1}
        self.res = 0
        def dfs(node):
            if node in cache:
                return cache[node]
            
            l = 1+dfs(node.left)
            r = 1+dfs(node.right)
            cache[node] = max(l,r)
            self.res = max(self.res, l+r)
            
            return cache[node]
        
        dfs(root)
        return self.res
            
            
            
            
            
            
          