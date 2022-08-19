# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        l = r = head
        
        while r and r.next:
            l = l.next
            r = r.next.next
        
        cur = l.next
        l.next = None
        
        #reverse the list
        prev = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        r = prev
        cur = head
        
        while r and cur:
            nxt = cur.next
            rnxt = r.next
            
            cur.next = r
            r.next = nxt
            
            cur = nxt
            r = rnxt
            