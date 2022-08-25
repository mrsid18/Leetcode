# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, n1: Optional[TreeNode], n2: Optional[TreeNode]) -> bool:
        if n1 and n2: return n1.val==n2.val and self.isSameTree(n1.left, n2.left) and self.isSameTree(n1.right, n2.right)
        if not n1 and not n2: return True
        return False