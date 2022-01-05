# Bubble Sort
# https://www.algoexpert.io/questions/Bubble%20Sort

import unittest

# Best O(N) time | O(1) space
# Avg. O(N^2) time | O(1) space
# Max. O(N^2) time | O(1) space
def bubbleSort(array):
    upto_index = len(array)
    for _ in range(len(array)):
        upto_index -= 1
        swapped = False
        for i in range(upto_index):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                swapped = True
        if not swapped:
            return array
    return array

class TestProgram(unittest.TestCase):
	def test_case(self):
		self.assertEqual(bubbleSort([8, 5, 2, 9, 5, 6, 3]), [2, 3, 5, 5, 6, 8, 9])
		self.assertEqual(bubbleSort([1]), [1])
		self.assertEqual(bubbleSort([1, 3, 2]), [1, 2, 3])
		self.assertEqual(bubbleSort([3, 1, 2]), [1, 2, 3])
		self.assertEqual(bubbleSort([1, 2, 3]), [1, 2, 3])
		self.assertEqual(bubbleSort([-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7, -6, -7, 8]), sorted([-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7, -6, -7, 8]))

if __name__=='__main__':
	unittest.main()
