# Longest Common Prefix [LeetCode]
# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        longest_common_prefix = ""
        min_element = min(strs, key=len)
        
        for i in range(len(min_element)):
            if len(set([word[i] for word in strs])) == 1:
                longest_common_prefix += strs[0][i]
            else:
                break
            
        return longest_common_prefix

#######################################################################

import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(Solution().longestCommonPrefix(["dog","racecar","car"]), "")
        self.assertEqual(Solution().longestCommonPrefix(["flower","flow","flight"]), "fl")

if __name__=='__main__':
    unittest.main()