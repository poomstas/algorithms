# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = self.getTreePaths(root, [], [])
        return ['->'.join(path) for path in paths]
    
    def getTreePaths(self, node, current_path, paths):
        if node is None:
            return paths
        
        current_path.append(str(node.val))
        
        if node.left is None and node.right is None:
            paths.append(current_path[:])
            current_path.pop()
            return paths
        
        paths = self.getTreePaths(node.left, current_path, paths)
        paths = self.getTreePaths(node.right, current_path, paths)
        current_path.pop()
        
        return paths