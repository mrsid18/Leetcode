# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, pre: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(i):
            if not i: return
            p = pre.pop(0)
            idx = i.index(p)
            
            cur = TreeNode(p)
            cur.left = dfs(i[:idx])
            cur.right = dfs(i[idx+1:])
            
            return cur
        return dfs(inorder)
            
            
            
        
        
        
        