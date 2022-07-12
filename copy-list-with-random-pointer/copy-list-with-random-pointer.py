"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        
        # Create weaved list (A -> A' -> B -> B' -> ...)
        # Here, A'.random points to the same node as A.random
        while curr is not None:
            curr.next = Node(x=curr.val, next=curr.next, random=curr.random)
            curr = curr.next.next
        
        # Update the random pointers
        curr = head
        out = head.next if head else None
        while curr is not None:
            next_hold = curr.next
            next_hold.random = next_hold.random.next if next_hold.random else None
            curr = curr.next.next if curr.next else None
        
        # Update the next pointers
        curr = out
        while curr is not None:
            curr.next = curr.next.next if curr.next else None
            curr = curr.next
        return out
    
    # FYI, the solution above modifies the original linked list but does not revert it back to its original state.
    
    def printRandomList(self, head):
        curr = head
        out = []
        while curr is not None:
            out.append([curr.val, hex(id(curr.random))])
            curr = curr.next
        print(out)
