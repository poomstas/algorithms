# Roman to Integer [LeetCode]
# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000 }
        
        number = 0
        prev_num = 0 # Anything that's smaller than 1
        
        for character in reversed(s): # Reversed order is key to making it simpler
            current_num = symbols[character]
            if current_num >= prev_num:
                number += current_num
            else:
                number -= current_num
            prev_num = current_num
        return number

#######################################################################

import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.romanToInt("III"), 3)
        self.assertEqual(sol.romanToInt("LVIII"), 58)
        self.assertEqual(sol.romanToInt("MCMXCIV"), 1994)

if __name__=='__main__':
    unittest.main()