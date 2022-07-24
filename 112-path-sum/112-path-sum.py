# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.checkPathSum(root, targetSum)
    
    def checkPathSum(self, node, targetSum, runningSum=0):
        if node is None:
            return False
        
        runningSum += node.val
        
        if node.left is None and node.right is None:
            return runningSum == targetSum
        
        L_has_pathsum = self.checkPathSum(node.left, targetSum, runningSum)
        R_has_pathsum = self.checkPathSum(node.right, targetSum, runningSum)
        
        return L_has_pathsum or R_has_pathsum
            
        