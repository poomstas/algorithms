# Spiral Traverse 
# https://www.algoexpert.io/questions/Spiral%20Traverse

import unittest

def spiralTraverse(array):
	i, j = 0, 0 # Current Position
	I, J = len(array[0]), len(array)
	visited = [[False for col in row] for row in array]
	total_steps = I * J
	output = []
	direction = 'right'
	count = 0
	while count < total_steps:
		count += 1
		output.append(array[j][i])
		visited[j][i] = True
		(i, j), direction = getNextPosition(i, j, I, J, visited, direction)
	return output

def getNextPosition(i, j, I, J, visited, direction):
	if direction == 'right':
		if i==I-1 or visited[j][i+1]: # If the next one is out of bounds or visited
			return (i, j+1), 'down'
		else:
			return (i+1, j), 'right'
	if direction == 'down':
		if j==J-1 or visited[j+1][i]: # If the next one is out of bounds or visited
			return (i-1, j), 'left'
		else:
			return (i, j+1), 'down'
	if direction == 'left':
		if i==0 or visited[j][i-1]: # If the next one is out of bounds or visited
			return (i, j-1), 'up'
		else:
			return (i-1, j), 'left'
	if direction == 'up':
		if j==0 or visited[j-1][i]: # If the next one is out of bounds or visited
			return (i+1, j), 'right'
		else:
			return (i, j-1), 'up'

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        matrix = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        self.assertEqual(spiralTraverse(matrix), expected)

if __name__=='__main__':
    unittest.main()