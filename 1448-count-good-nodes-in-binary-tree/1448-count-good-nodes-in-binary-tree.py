# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        output = []
        def test(node,path):
            if not node:
                return
            
            path.append(node.val)
            # print(path)
            if max(path)<=node.val:
                output.append(node.val)
            test(node.left, path[:])
            test(node.right, path[:])
        
        test(root, [])
        # print(output)
        return len(output)
            
                
        