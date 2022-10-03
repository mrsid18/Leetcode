"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        stack = []
        
        cur = head
        prev = cur
        
        while cur or stack:
            if not cur:
                cur = prev
                cur.next = stack.pop()
                cur.next.prev = cur   
            elif cur.child:
                if cur.next: stack.append(cur.next)
                cur.next = cur.child
                cur.child.prev = cur
                cur.child = None
            
            prev = cur
            cur = cur.next
           
            
        return head
        