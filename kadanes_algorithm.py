# Kadane's Algorithm
# https://www.algoexpert.io/questions/Kadane's%20Algorithm

import unittest


def kadanesAlgorithm(array):
    maxEndingHere = array[0]
    maxSoFar = array[0]
    for value in array[1:]:
        maxEndingHere = max(value, maxEndingHere + value)
        maxSoFar = max(maxSoFar, maxEndingHere)
    return maxSoFar


#######################################################################


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            kadanesAlgorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]), 19
        )


if __name__ == "__main__":
    unittest.main()
