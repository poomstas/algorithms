# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.paths = []
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.checkPathSum(root, targetSum)
        return self.paths
    
    def checkPathSum(self, node, targetSum, runningList=[]):
        if node is None:
            return
        
        runningList.append(node.val)
        
        if node.left is None and node.right is None:
            if sum(runningList) == targetSum:
                self.paths.append(runningList[:]) # Need to make a copy of the list before appending
            runningList.pop()
            return
        
        self.checkPathSum(node.left, targetSum, runningList)
        self.checkPathSum(node.right, targetSum, runningList)
        runningList.pop()
        return
