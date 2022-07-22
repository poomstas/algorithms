# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        next_queue = deque([root])
        output = []
        
        while next_queue:
            queue = next_queue
            next_queue = deque()
            current_level_vals = []
            
            while queue:
                node = queue.popleft()
                current_level_vals.append(node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)

            output.append(current_level_vals)
            
        return output