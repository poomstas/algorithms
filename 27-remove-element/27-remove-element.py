class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a, b = 0, len(nums)-1
        while a <= b:
            val_a, val_b = nums[a], nums[b]
            if val_a==val and val_b!=val:
                nums[a], nums[b] = val_b, val_a 
                a += 1
                b -= 1
            elif val_a!=val and val_b==val:
                a += 1
                b -= 1
            elif val_a!=val and val_b!=val:
                a += 1
            else:
                b -= 1
        return a
    
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         a, b = 0, len(nums)-1
#         while a <= b:
#             if nums[a]==val and nums[b]!=val:
#                 nums[a], nums[b] = nums[b], nums[a]
#                 a += 1
#                 b -= 1
#             elif nums[a]!=val and nums[b]==val:
#                 a += 1
#                 b -= 1
#             elif nums[a]!=val and nums[b]!=val:
#                 a += 1
#             else:
#                 b -= 1
#         return a
