# Definition for a binary tree node.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def md(self, root):
        if root is None:
            return
        
        self.md(root.left)
        self.md(root.right)
    
    def maxDepth(self, root):
        if not root:
            return 0
        depth = 0
        que = deque([root])
        
        while que:
            length = len(que)
            for i in range(length):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            depth+=1
        
        return depth
                
        
        
     