# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
        def isSameTree(n1, n2):
            if n1 and n2:
                return n1.val==n2.val and isSameTree(n1.left, n2.left) and isSameTree(n1.right, n2.right)
            if not n1 and not n2:
                return True
            return False
        
        self.res = False
        
        def traverse(node):
            if not node: return
            
            if node.val == t.val:
                self.res |= isSameTree(node, t)
            
            traverse(node.left)
            traverse(node.right)
        
        traverse(s)
        return self.res
                
            