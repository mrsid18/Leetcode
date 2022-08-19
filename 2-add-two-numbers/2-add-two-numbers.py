# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c = 0
        
        cur = ListNode()
        res = cur
        
        while l1 and l2:
            total = l1.val + l2.val + c
            c=0
            if total>9:
                total -= 10
                c = 1
            cur.next = ListNode(total)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            total = l1.val + c
            c=0
            if total>9:
                total -= 10
                c = 1
            cur.next = ListNode(total)
            cur = cur.next
            l1 = l1.next
        
        while l2:
            total = l2.val + c
            c=0
            if total>9:
                total -= 10
                c = 1
            cur.next = ListNode(total)
            cur = cur.next
            l2 = l2.next
        
        if c: 
            cur.next = ListNode(1)
        
        return res.next
            