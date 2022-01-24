class Solution:
    # O(n) time | O(n) space
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        visited = {}
        for i, num in enumerate(nums):
            other_num = target - num
            if other_num in visited:
                return [i, visited[other_num]]
            visited[num] = i
        
#######################################################################

import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(Solution().twoSum([2,7,11,15], 9), [1, 0])

if __name__=='__main__':
    unittest.main()