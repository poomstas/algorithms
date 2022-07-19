# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, node):
        
        def traverse(node, output):
            if node is None:
                return
            traverse(node.left, output)
            output.append(node.val)
            traverse(node.right, output)
            return output
        
        output = []
        output = traverse(node, output)
        
        return output
