# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.getDiameter(root).diameter
        
    def getDiameter(self, node):
        if node is None:
            return TreeInfo(0, 0)
        
        L = self.getDiameter(node.left)
        R = self.getDiameter(node.right)
        
        diameter = max(L.diameter, R.diameter, L.height + R.height)
        height = max(L.height, R.height) + 1
        
        return TreeInfo(diameter, height)


class TreeInfo:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height
        