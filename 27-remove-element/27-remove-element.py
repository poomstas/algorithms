class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a, b = 0, len(nums)-1
        while a <= b:
            if nums[a]==val and nums[b]!=val:
                nums[a], nums[b] = nums[b], nums[a]
                a += 1
                b -= 1
            elif nums[a]!=val and nums[b]==val:
                a += 1
                b -= 1
            elif nums[a]!=val and nums[b]!=val:
                a += 1
            else:
                b -= 1
        return a
