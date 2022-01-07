# Binary Search
# https://www.algoexpert.io/questions/Binary%20Search

import unittest

# O(log(N)) Time | O(1) Space
def binarySearch(array, target):
	L, R = 0, len(array)-1
	while L <= R:
		M = (L+R)//2
		if array[M] > target:
			R = M-1
		elif array[M] < target:
			L = M+1
		elif array[M] == target:
			return M
	return -1

######################################################################3

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33), 3)

if __name__=='__main__':
	unittest.main()
