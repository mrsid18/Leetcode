# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # O(logn) to find an element
        # so we need to know all the elements
        
        # iterative
        cur = root
        stack = []
        n = 0
        
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            n+=1
            
            if n==k:
                return cur.val
            
            cur = cur.right
        
        
        # recursive
        
        res = []
        def dfs(node):
            if not node:
                return 
            
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
            
        dfs(root)
        
        return res[k-1]
            