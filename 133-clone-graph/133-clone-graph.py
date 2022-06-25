"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        hmap = {}
        
        def dfs(node):
            if node in hmap:
                return hmap[node]
            
            clone = Node(node.val)
            hmap[node] = clone
            
            for n in node.neighbors:
                clone.neighbors.append(dfs(n))
            
            return clone
        
        return dfs(node) if node else None