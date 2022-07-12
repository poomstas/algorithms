# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTHelper(root)
      
    def isValidBSTHelper(self, node, leftmax=float('inf'), rightmin=-float('inf')):
        if node is None:
            return True
        
        if node.val >= leftmax or node.val <= rightmin:
            return False
        
        L_valid = self.isValidBSTHelper(node.left, node.val, rightmin)
        R_valid = self.isValidBSTHelper(node.right, leftmax, node.val)
        
        return L_valid and R_valid