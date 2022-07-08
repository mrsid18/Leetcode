# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #length of left side + max length of right side
        
        self.res = 0
        def dfs(node):
            if not node:
                return -1
            
            l = 1+dfs(node.left)
            r = 1+dfs(node.right)
            self.res = max(self.res, l+r)
            
            return max(l, r)
        
        dfs(root)
        return self.res
            
            
            
            
            
            
          