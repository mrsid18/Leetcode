# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getKth(self, node, k):
        while node and k:
            node = node.next
            k-=1
        return node
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        
        while True:
            kth = self.getKth(groupPrev, k)
            
            if not kth:
                break
            
            groupNext = kth.next
            
            prev, cur = groupNext, groupPrev.next
            
            while cur!=groupNext:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur =tmp
            
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
            
        
        return dummy.next
            
        
        
        