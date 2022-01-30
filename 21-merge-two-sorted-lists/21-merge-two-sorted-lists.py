# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current_node_1, current_node_2 = list1, list2
        if list1 is None and list2 is None:
            return None
        output = ListNode()
        current_node_out = output
        
        while current_node_1 is not None or current_node_2 is not None:
            #current_node_out = ListNode() if current_node_out is None else current_node_out.next
            
            val_1 = current_node_1.val if current_node_1 is not None else float('inf')
            val_2 = current_node_2.val if current_node_2 is not None else float('inf')
            
            if val_1 <= val_2:
                current_node_out.val = val_1
                current_node_1 = current_node_1.next
            else:
                current_node_out.val = val_2
                current_node_2 = current_node_2.next
                
            if current_node_1 is not None or current_node_2 is not None:
                current_node_out.next = ListNode()
                current_node_out = current_node_out.next
                
        return output
        
        