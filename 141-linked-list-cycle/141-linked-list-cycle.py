# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hmap = set()
        
        while head:
            if head in hmap:
                return True
            hmap.add(head)
            head = head.next
        
        return False
        
        
        #2 pointers
        f, s = head, head
        
        while f and f.next:
            f=f.next.next
            s=s.next
            if f==s:
                return True
        
        return False