# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.helper(nums, 0, len(nums)-1)
        
    def helper(self, nums, L, R):
        if L > R:
            return None
        
        M = (L + R) // 2
        node = TreeNode(nums[M])
        node.left = self.helper(nums, L, M-1)
        node.right = self.helper(nums, M+1, R)
        
        return node