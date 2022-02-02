# O(N) time | O(N) space
def sortedSquaredArray(array):
    L, R = 0, len(array)-1
    output = [0 for _ in array] # Initialize empty array

    for i in reversed(range(len(output))):

        Lval, Rval = array[L], array[R]

        if abs(Lval) < abs(Rval):
            R -= 1
            output[i] = Rval ** 2
        else:
            L +=1 
            output[i] = Lval ** 2

    return output

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