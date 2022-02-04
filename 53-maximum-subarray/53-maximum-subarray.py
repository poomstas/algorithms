class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Algorithm
        
        maxEndingHere = nums[0]
        maxSoFar = nums[0]
        
        for value in nums[1:]:
            maxEndingHere = max(value, maxEndingHere+value)
            maxSoFar = max(maxSoFar, maxEndingHere)
            
        return maxSoFar
        