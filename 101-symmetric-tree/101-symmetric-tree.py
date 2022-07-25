# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = deque([[root, root]])
        while queue:
            item = queue.popleft()
            nodeA, nodeB = item
            if nodeA is None and nodeB is not None:
                return False
            if nodeA is not None and nodeB is None:
                return False
            if nodeA is None and nodeB is None:
                continue
            if nodeA.val != nodeB.val:
                return False
            queue.append([nodeA.left, nodeB.right])
            queue.append([nodeA.right, nodeB.left])
        return True
