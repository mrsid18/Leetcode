# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,node, pos, level ,output):
        if not node:
            return None
        
        output.append(str(node.val)+pos+str(level))
        self.dfs(node.left, 'l', level+1, output)
        self.dfs(node.right, 'r', level+1, output)
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        out1,out2 = [],[]
        self.dfs(p, 'l', 0, out1)
        self.dfs(q, 'l', 0, out2)
        return out1==out2
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
                