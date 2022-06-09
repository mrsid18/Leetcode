# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #simple traversal problem
        lo = []
        ro = []
        def lfs(node):
            if not node:
                lo.append(None)
                return
            
            lo.append(node.val)
            lfs(node.left)
            lfs(node.right)
            
        def rfs(node):
            if not node:
                ro.append(None)
                return
            
            ro.append(node.val)
            rfs(node.right)
            rfs(node.left)
            
        lfs(root.left)
        rfs(root.right)
        
        return lo==ro
            
            
            
            
            
            
        