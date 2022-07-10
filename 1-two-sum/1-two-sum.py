class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: # Single pass hash
        # O(N) time | O(N) space
        seen = {} # value:index format
        for i, val in enumerate(nums):
            complement = target - val
            if complement in seen:
                return [i, seen[complement]]
            seen[val] = i
        
    def twoSumAlt2(self, nums: List[int], target: int) -> List[int]: # Two pass hash
        # O(N) time | O(N) space
        seen = {} # value:index format
        for i, val in enumerate(nums):
            seen[val] = i
        for i, val in enumerate(nums):
            complement = target - val
            if complement in seen and seen[complement]!=i:
                return [i, seen[complement]]
