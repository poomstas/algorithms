class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return nums
        
        i, j = 0, 1
        while i < len(nums) and j < len(nums):
            a, b = nums[i], nums[j]
            
            if a==0 and b!=0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif a==0 and b==0:
                j += 1
            else:
                i += 1
                j += 1
                
        return nums
