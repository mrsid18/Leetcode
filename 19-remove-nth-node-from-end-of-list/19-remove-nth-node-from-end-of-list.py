# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
#         1 2 3 4 5
#           1 2 3 4
#         5-1+1 = 5
#         5-2+1 = 4
#         5-5+1 = 1
        
        #find the length of the linked list
        #simply remove that 
        
        cur = head
        length = 0
        
        while cur:
            cur = cur.next
            length+=1
        
        nth = length - n + 1
        
        if nth==1: return head.next
        
        i = 1
        cur = head
        while i!=nth-1:
            cur = cur.next
            i+=1
        
        cur.next = cur.next.next
        
        return head
        
        
        