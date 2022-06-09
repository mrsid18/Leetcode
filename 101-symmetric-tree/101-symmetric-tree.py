# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lsf(self, root, output, s):
        if not root:
            return 
        
        output.append(str(root.val)+s)
        self.lsf(root.left, output, 'l')
        self.lsf(root.right, output, 'r')
        
    def rsf(self, root, output, s):
        if not root:
            return 
        
        output.append(str(root.val)+s)
        self.rsf(root.right, output, 'l')
        self.rsf(root.left, output, 'r')
        
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        if not root.left and not root.right:
            return True
        
        if not root.left or not root.right:
            return False
        
        leftList = []
        self.rsf(root, leftList, '')
        
        rightList = []
        self.lsf(root, rightList, '')
        
        print(leftList, rightList)
        
        if len(leftList) != len(rightList):
            return False
        
        # for idx,lnum in enumerate(leftList):
        if str(leftList) != str(rightList):
                return False
        
        return True
        
        