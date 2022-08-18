# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def dfs(cur, prev):
            if not cur: return prev
            
            nxt = cur.next
            cur.next = prev
            return dfs(nxt, cur)
        
        return dfs(head, None)
        
#         prev, cur = None, head
        
#         while cur:
#             nxt = cur.next
#             cur.next = prev
#             prev = cur
#             cur = nxt
        
#         return prev
    
        
            
        
        