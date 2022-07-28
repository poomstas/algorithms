# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced, height = self.checkBalanced(root)
        return balanced
    
    def checkBalanced(self, node):
        if node is None:
            return True, 0
        
        L_balanced, L_height = self.checkBalanced(node.left)
        R_balanced, R_height = self.checkBalanced(node.right)
        
        balanced = abs(L_height - R_height) <= 1 and L_balanced and R_balanced
        height = max(L_height, R_height) + 1
        
        return balanced, height