# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def dfs(node):
            if not node:
                res.append(None)
                return
            
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return ','.join([str(r) for r in res])
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        self.i = 0
        
        def dfs():
            if vals[self.i]=='None':
                self.i+=1
                return None
            
            cur = TreeNode(int(vals[self.i]))
            self.i+=1
            cur.left = dfs()
            cur.right = dfs()
            
            return cur 
        
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))