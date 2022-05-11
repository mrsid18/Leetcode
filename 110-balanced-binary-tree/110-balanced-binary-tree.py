# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def verify(node):
            if node is None:
                return [True,-1]
            
            l,lh = verify(node.left)
            r,rh = verify(node.right)
            return [l and r and abs(lh-rh)<=1,max(lh+1,rh+1)]
        
        return verify(root)[0]