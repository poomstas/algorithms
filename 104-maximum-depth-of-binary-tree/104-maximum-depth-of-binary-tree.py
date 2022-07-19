# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, node, depth=1) -> int:
        if node is None:
            if depth==1:
                return 0
            else:
                return depth
        
        depth_L = self.maxDepth(node.left, depth+1) if node.left is not None else depth
        depth_R = self.maxDepth(node.right, depth+1) if node.right is not None else depth
            
        return max(depth_L, depth_R)
        