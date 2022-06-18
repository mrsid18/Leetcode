"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        random = {None: None}
        
        cur = head
        dummy = Node(0)
        ncur = dummy
        
        while cur:
            ncur.next = Node(cur.val, cur.next)
            random[cur] = ncur.next
            cur = cur.next
            ncur = ncur.next
        
        cur = head 
        ncur = dummy.next
        
        while cur:
            ncur.random = random[cur.random]
            ncur = ncur.next
            cur = cur.next
        
        return dummy.next
            