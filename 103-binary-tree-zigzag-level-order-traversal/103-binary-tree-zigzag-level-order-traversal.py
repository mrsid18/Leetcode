# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 1. initialize queue
        # 2. add root node to queue
        # 3. iterate through the queue nodes/ pop them and 
        #     add their respective left and right nodes
        # 4. Add the popped nodes to the list
        # And that's it
        if root is None:
            return
        queue = deque([root])
        output = []
        left = True
        while queue:
            temp = []
            length = len(queue)
            
            for i in range(length):
                if left:
                    node = queue.popleft()
                else:
                    node = queue.pop()
                    
                temp.append(node.val)
                if left:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                else:
                    if node.right:
                        queue.appendleft(node.right)
                    if node.left:
                        queue.appendleft(node.left)
                    
                    
            output.append(temp)
            left = (not left)
            
        return output
                    
        
                
        