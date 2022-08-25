# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = -inf
        def maxD(node):
            if not node: return -1
            l = 1+maxD(node.left)
            r = 1+maxD(node.right)
            self.res = max(self.res, l+r)
            return max(l,r)
        maxD(root)
        return self.res
            
            
            
            
          