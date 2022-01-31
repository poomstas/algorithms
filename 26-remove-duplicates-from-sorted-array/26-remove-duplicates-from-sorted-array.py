class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a, b = 0, 0
        for _ in range(len(nums)):
            if nums[a]==nums[b]:
                b += 1
            else:
                a += 1
                nums[a] = nums[b]
                b += 1
        return a+1
                
        