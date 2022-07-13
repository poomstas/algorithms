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
        queue = deque([root, None,])
        rightside = []
        curr = root
        
        while queue:
            prev, curr = curr, queue.popleft()
            
            while curr:
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                    
                prev, curr = curr, queue.popleft()
                
            rightside.append(prev.val)
            
            if queue:
                queue.append(None)
                
        return rightside
        