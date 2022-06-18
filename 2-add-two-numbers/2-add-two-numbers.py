# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        res = ListNode()
        cur = res
        
        while l1 and l2:
            cur.next = ListNode((l1.val+l2.val+carry)%10)
            carry = (l1.val+l2.val+carry)//10
            l1 = l1.next
            l2 = l2.next
            cur = cur.next
        
        node = l1 or l2
        
        while node:
            cur.next = ListNode((node.val+carry)%10)
            carry = (node.val+carry)//10
            node = node.next
            cur = cur.next
        
        if carry:
            cur.next = ListNode(1)
        
        return res.next
        
        