# Smallest Difference
# https://www.algoexpert.io/questions/Smallest%20Difference

import unittest

# nlog(n) + mlog(m) time | O(1) space
def smallestDifference(arrayOne, arrayTwo):
    min_diff = float('inf')
    arrayOne.sort() # Sort in-place, O(Nlog(N))
    arrayTwo.sort() # Sort in-place, O(Nlog(N))
    
    i_one, i_two = 0, 0

    while i_one < len(arrayOne) and i_two < len(arrayTwo):

        valOne, valTwo = arrayOne[i_one], arrayTwo[i_two]
        current_diff = abs(valOne-valTwo)

        if current_diff < min_diff:
            min_diff = current_diff
            finalOne, finalTwo = valOne, valTwo

        if valOne > valTwo:
            i_two += 1
        elif valOne < valTwo:
            i_one += 1
        else:
            return (valOne, valTwo)

    return [finalOne, finalTwo]

#####################################################################

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]), [28, 26])

if __name__=='__main__':
    unittest.main()
