class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums) # O(Nlog(N)) time
        out = []
        prev_val = -float('inf')
        for i, fixed_val in enumerate(nums):
            if fixed_val > 0:
                break
            if prev_val == fixed_val:
                continue
            prev_val = fixed_val
            self.twoSum(nums, i, out)
        return out
            
    def twoSum(self, nums, first_i, out):
        target = -nums[first_i]
        i, j = first_i+1, len(nums)-1
        while i < j:
            a, b = nums[i], nums[j]
            if a+b < target:
                i += 1
            elif a+b > target:
                j -= 1
            else:
                out.append([nums[first_i], a, b])
                i += 1
                j -= 1
                while i < j and nums[i] == nums[i-1]:
                    i += 1
