# O(N + M) time | O(1) space complexity
def searchInSortedMatrix(matrix, target):
    nRow, nCol = len(matrix), len(matrix[0])
    row, col = 0, nCol-1

    while row < nRow and col >= 0:
        current_no = matrix[row][col]

        if current_no > target:
            col -= 1
        elif current_no < target:
            row += 1
        else:
            return [row, col]

    return [-1, -1]

#######################################################################

import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        matrix = [
            [1, 4, 7, 12, 15, 1000],
            [2, 5, 19, 31, 32, 1001],
            [3, 8, 24, 33, 35, 1002],
            [40, 41, 42, 44, 45, 1003],
            [99, 100, 103, 106, 128, 1004],
        ]
        actual = searchInSortedMatrix(matrix, 44)
        self.assertEqual(actual, [3, 3])

if __name__=='__main__':
	unittest.main()
