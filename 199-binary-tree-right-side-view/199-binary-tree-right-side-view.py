# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        next_queue = deque([root])
        output_list = []
        
        while next_queue:
            queue, next_queue = next_queue, deque([])
            
            while queue:
                node = queue.popleft()
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
                
            output_list.append(node.val)
            
        return output_list
                
        