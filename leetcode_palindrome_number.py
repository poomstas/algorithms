class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]

#######################################################################

import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(Solution().isPalindrome(121), True)

if __name__=='__main__':
    unittest.main()