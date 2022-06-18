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
        while len(lists)>1:
            lists.append(self.merge2lists(lists.pop(), lists.pop()))
        
        return lists[0]