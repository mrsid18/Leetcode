# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, output, level=0, direc='t'):
        if root is None:
            return
        
        output.append(str(root.val)+direc+str(level))
        level+=1
        self.traverse(root.left, output, level, 'l')
        self.traverse(root.right, output, level, 'r')
        
    def compare(self, root):
        if root is None:
            return 
        
        rootTraverse = []
        self.traverse(root, rootTraverse)
        if rootTraverse == self.subRootArr:
            return True
        left = self.compare(root.left)
        if left:
            return True
        right = self.compare(root.right)
        if right:
            return True
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.subRootArr = []
        self.traverse(subRoot, self.subRootArr)
        
        return self.compare(root)