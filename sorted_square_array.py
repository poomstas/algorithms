# O(N) time | O(N) space
def sortedSquaredArray(array):
	output_array = [0] * len(array) # Initialize output array
	pointer = len(array)-1 # Pointer for the output array
	L, R = 0, len(array)-1
	
	while L <= R:
		Lval, Rval = array[L], array[R]
		if abs(Lval) < abs(Rval):
			R -= 1
			output_array[pointer] = Rval**2
		else:
			L += 1
			output_array[pointer] = Lval**2
		pointer -= 1
		
	return output_array

#######################################################################

import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [1, 2, 3, 5, 6, 8, 9]
        expected = [1, 4, 9, 25, 36, 64, 81]
        actual = sortedSquaredArray(input)
        self.assertEqual(actual, expected)

if __name__=='__main__':
	unittest.main()