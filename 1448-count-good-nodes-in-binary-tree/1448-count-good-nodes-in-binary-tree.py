# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.output = 0
        def test(node,maxVal):
            if not node:
                return
            
            if maxVal<=node.val:
                self.output += 1
                maxVal = node.val
            
            test(node.left, maxVal)
            test(node.right, maxVal)
        
        test(root, root.val)
        # print(output)
        return self.output
            
                
        