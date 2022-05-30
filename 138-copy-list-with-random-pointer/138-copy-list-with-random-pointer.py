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
        if not head:
            return
        cur = head
        
        while cur:
            p = Node(cur.val)
            p.next = cur.next
            cur.next = p
            cur = p.next
        
        p1, p2 = head, head.next
        res = head.next
        while p1:
            next1 = p1.next.next
            p2.next = p2.next.next if p2.next else None
            p2.random = p1.random.next if p1.random else None
            p1 = next1
            p2 = p2.next
        
        return res
            
        