# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return
        
        p1 = head
        p2 = head.next.next
        
        if not (p1 and p2):
            return
        while p2:
            p1 = p1.next
            p2 = p2.next.next if p2.next else None
        
        temp = p1.next
        p1.next = None
        p1 = temp
        
        #reverse a linked list
        p2 = p1.next
        p1.next = None
        
        while p2:
            temp = p2.next
            p2.next = p1
            p1 = p2
            p2 = temp
        temp = head.next
        while p1:
            temp = head.next
            head.next = p1
            temp1 = p1.next
            p1.next = temp
            head = temp
            p1 = temp1
        