# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge2lists(self,l1, l2):
        node = ListNode()
        head = node
        while l1 and l2:
            if l1.val>l2.val:
                node.next = l2
                l2 = l2.next
            else:
                node.next = l1
                l1=l1.next
            node = node.next
        
        if l1:
            node.next = l1
        if l2:
            node.next = l2
        
        return head.next
                
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return 
        
        cur = lists[0]
        
        for i in range(1, len(lists)):
            cur = self.merge2lists(cur, lists[i])
        
        return cur
            