# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         self.maxLen = []
#         def maxDepth(node):
#             if node is None:
#                 return 0
            
#             return 1+max(maxDepth(node.left), maxDepth(node.right))
        
#         def traverse(node, length):
#             if node:
#                 length = max((maxDepth(node.left)+maxDepth(node.right)), length)
#                 self.maxLen.append(length)
#                 traverse(node.left, length)
#                 traverse(node.right, length)
#         traverse(root, 0)
#         return max(self.maxLen)
          
          self.max = 0
          
          def traverse(node):
            if node is None:
                return -1
            left = traverse(node.left)
            right = traverse(node.right)
            
            self.max = max(self.max, 2+left+right)
            
            return 1+max(left, right)
        
          traverse(root)
          return self.max
            
          