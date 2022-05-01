# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        t1 = head
        t2 = head.next
        head.next = None
        while t2:
            temp = t2.next
            t2.next = t1
            t1 = t2
            t2 = temp
        
        return t1
            