# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, node, depth=0) -> int:
        if node is None:
            return depth
        
        depth += 1
        depth_L = self.maxDepth(node.left, depth) if node.left is not None else depth
        depth_R = self.maxDepth(node.right, depth) if node.right is not None else depth
            
        return max(depth_L, depth_R)
