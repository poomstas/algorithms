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
            return
        
        runningSum += node.val
        
        if node.left is None and node.right is None:
            return targetSum == runningSum
        
        L_path_sum = self.checkPathSum(node.left, targetSum, runningSum)
        R_path_sum = self.checkPathSum(node.right, targetSum, runningSum)
        
        return L_path_sum or R_path_sum
            