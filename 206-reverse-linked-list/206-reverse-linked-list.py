# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(prev, cur):
            if not cur:
                return prev
            temp = cur.next
            cur.next = prev
            return reverse(cur, temp)
        
        return reverse(None, head)
            
        
        
        # iterative
        if not head:
            return
        
        p1, p2 = head, head.next
         
        while p2:
            temp = p2.next
            p2.next = p1
            p1 = p2
            p2 = temp
        
        head.next = None
        return p1
        
        