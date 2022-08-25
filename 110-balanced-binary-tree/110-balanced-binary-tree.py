# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def verify(node):
            if not node: return [True, -1]
            
            l, lh = verify(node.left)
            r, rh = verify(node.right)
            h = max(lh, rh)+1
            if abs(lh-rh)>1: return [False,h]
            
            return [l and r, h]
        
        return verify(root)[0]
            
            
            