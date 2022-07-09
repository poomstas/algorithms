# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        out = ListNode()
        curr = out
        
        while list1 is not None or list2 is not None:
            list1val = list1.val if list1 else float('inf')
            list2val = list2.val if list2 else float('inf')
            
            if list1val <= list2val:
                curr.next = ListNode(list1val)
                list1 = list1.next if list1 else None
            else:
                curr.next = ListNode(list2val)
                list2 = list2.next if list2 else None
            curr = curr.next
                
        return out.next
        