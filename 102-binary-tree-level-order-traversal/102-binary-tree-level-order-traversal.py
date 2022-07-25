# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        next_queue = deque([root])
        while next_queue:
            queue, next_queue = next_queue, deque([])
            current_level_vals = []
            while queue:
                node = queue.popleft()
                if node is None:
                    continue
                current_level_vals.append(node.val)
                next_queue.extend([node.left, node.right])
            if current_level_vals != []:
                output.append(current_level_vals)
        return output
