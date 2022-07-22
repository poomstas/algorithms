# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.getMaxDepth(root)
        
    def getMaxDepth(self, node, depth=0):
        if node is None:
            return depth
        
        L = self.getMaxDepth(node.left, depth+1)
        R = self.getMaxDepth(node.right, depth+1)
        depth = max(L, R)
        
        return depth
        
        