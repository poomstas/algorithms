# Two Number Sum
# https://www.algoexpert.io/questions/Two%20Number%20Sum

import unittest

# O(N) time | O(N) space
# O(N) space because we're storing the values in a separate dictionary
def twoNumberSum(array, targetSum):
	nums = {}
	for num in array:
		potentialMatch = targetSum - num
		if potentialMatch in nums:
			return [num, potentialMatch]
		else:
			nums[num] = True
	return []

# O(Nlog(N)) time | O(1) space
def twoNumberSum(array, targetSum):
	array.sort() # Assume python uses an optimal sorting algo (Quicksort or Mergesort) -> O(Nlog(N)) 
	L_indx, R_indx = 0, len(array)-1

	while L_indx < R_indx:
		L, R = array[L_indx], array[R_indx]
		currentSum = L + R
		if currentSum == targetSum:
			return [L, R]
		elif currentSum < targetSum:
			L_indx += 1
		elif currentSum > targetSum:
			R_indx -= 1
	return []

class TestProgram(unittest.TestCase):
	def test_case(self):
		self.assertEqual(sorted(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10)), [-1, 11])

		output = twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10) 
		self.assertTrue(len(output) == 2)
		self.assertTrue(11 in output)
		self.assertTrue(-1 in output)

if __name__=='__main__':
	unittest.main()
