# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,node1, node2):
        if node1 == node2:
            return True
        
        if node1 and node2 and node1.val == node2.val:
            return (self.dfs(node1.left, node2.left) and self.dfs(node1.right, node2.right))
        else:
            return False
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.dfs(p,q)
        que1,que2 = [], []
        if p:
            que1 = deque([[p,'l']])
        if q:
            que2 = deque([[q,'l']])
        
        while que1:
            n1 = len(que1)
            n2 = len(que2)
            if n1!=n2:
                return False
            
            for i1 in range(n1):
                ele1,pos1 = que1.popleft()
                ele2,pos2 = que2.popleft()
                
                if ele1.val != ele2.val or pos1 != pos2 :
                    return False
                
                if ele1.left:
                    que1.append([ele1.left,'l'])
                if ele1.right:
                    que1.append([ele1.right,'r'])
                if ele2.left:
                    que2.append([ele2.left,'l'])
                if ele2.right:
                    que2.append([ele2.right,'r'])
                
                
        if que1 or que2:
                 return False
            
        return True
                