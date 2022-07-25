# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root, root)
        
    def isMirror(self, node_A, node_B):
        if node_A is None and node_B is None:
            return True
        if node_A is None or node_B is None:
            return False
        return node_A.val==node_B.val \
            and self.isMirror(node_A.right, node_B.left) \
            and self.isMirror(node_A.left, node_B.right)
