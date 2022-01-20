# Validate Subsequence
# https://www.algoexpert.io/questions/Validate%20Subsequence

def isValidSubsequence(array, sequence):
	seq_indx, done_indx = 0, len(sequence)
	
	for val in array:
		if val == sequence[seq_indx]:
			seq_indx += 1
		if seq_indx == done_indx:
			return True
	return False

#######################################################################

import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [1, 6, -1, 10]
        self.assertTrue(isValidSubsequence(array, sequence))

if __name__=='__main__':
	unittest.main()