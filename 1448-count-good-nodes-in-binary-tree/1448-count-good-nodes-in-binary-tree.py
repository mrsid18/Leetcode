# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        output = []
        def test(node,maxVal):
            if not node:
                return
            
            if maxVal<=node.val:
                output.append(node.val)
                maxVal = node.val
            
            test(node.left, maxVal)
            test(node.right, maxVal)
        
        test(root, root.val)
        # print(output)
        return len(output)
            
                
        