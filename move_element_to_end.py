# Move Element to End
# https://www.algoexpert.io/questions/Move%20Element%20To%20End

import unittest

# O(N) time | O(1) space
def moveElementToEnd(array, toMove):
	L, R = 0, len(array)-1
	while L < R:
		if array[L] != toMove:
			L += 1
		elif array[R] == toMove:
			R -= 1
		else:
			array[L], array[R] = array[R], array[L]
			L += 1
			R -= 1
	return array

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [2, 1, 2, 2, 2, 3, 4, 2]
        toMove = 2
        expectedStart = [1, 3, 4]
        expectedEnd = [2, 2, 2, 2, 2]
        output = moveElementToEnd(array, toMove)
        outputStart = sorted(output[0:3])
        outputEnd = output[3:]
        self.assertEqual(outputStart, expectedStart)
        self.assertEqual(outputEnd, expectedEnd)

if __name__=='__main__':
    unittest.main()