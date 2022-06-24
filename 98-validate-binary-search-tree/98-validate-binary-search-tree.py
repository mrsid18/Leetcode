# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
            # left hand side consists of -inf<node.val<min val
              # rhs cond. min val <
        def dfs(node, l, r):
            if not node:
                return True
            
            if l<node.val<r:
                return (dfs(node.left, l, node.val) and dfs(node.right, node.val, r))
            else: return False
        
        return dfs(root, -inf, inf)