# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1,p2 = head, head.next
        if not p2:
            return 
        m=0
        odd = 0
        while p2:
            m+=1
            p1 = p1.next
            if p2.next:
                p2 = p2.next.next
                odd = 1
            else:
                p2 = None
                odd = 0
        
        delete = 2*m + odd - n + 1
        
        if delete<=m+1:
            p1 = head
            m=0

        steps = delete-m-1
        if steps<=0:
            return head.next
        p2 = p1.next
        while steps>1:
            p2 = p2.next
            p1 = p1.next
            steps -= 1
    
        p1.next = p2.next
        return head
            
                
        # print(m,2*m+odd,p1)
        
#     def length(self, head: [ListNode]) -> int:
#         index=0
#         while head != None:
#             head=head.next
#             index+=1
            
#         return index
    
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
#         length = self.length(head)
#         index = length-n
#         temp = head
#         prev = head
#         idx=0
        
#         if index==0:
#             return temp.next
    
#         while idx<index:
#             prev=temp
#             temp = temp.next
#             idx+=1
        
#         prev.next = temp.next
        
#         return head
            
            
        