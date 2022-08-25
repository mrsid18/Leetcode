# Definition for a binary tree node.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root):
        def depth(node):
            if not node: return 0
            
            res = max(1+depth(node.left), 1+depth(node.right))
            return res
        
        return depth(root)
        