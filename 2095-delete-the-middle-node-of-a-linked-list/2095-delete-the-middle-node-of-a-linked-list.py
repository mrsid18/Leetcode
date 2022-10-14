# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next: return
        l, r = head, head
        prev = l
        while r and r.next:
            prev = l
            r = r.next.next
            l = l.next    
        
        prev.next = l.next
        return head