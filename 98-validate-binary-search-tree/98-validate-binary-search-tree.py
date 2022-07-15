# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validateBST(root)
    
    def validateBST(self, node, LB=-float('inf'), UB=float('inf')):
        # LB: Lower Bounds, UB: Upper Bounds. val should be in between.
        if node is None:
            return True
        
        if not (LB < node.val < UB):
            return False
    
        return self.validateBST(node.left, LB, node.val) and \
               self.validateBST(node.right, node.val, UB)