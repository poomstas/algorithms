# Branch Sums
# https://www.algoexpert.io/questions/Branch%20Sums

import unittest

def branchSums(root):
	sums = []
	calculateBranchSums(root, 0, sums)
	return sums

def calculateBranchSums(node, running_sum, sums):
	if node is None:
		return
	running_sum += node.value
	if node.left is None and node.right is None:
		sums.append(running_sum)
	
	calculateBranchSums(node.left, running_sum, sums)
	calculateBranchSums(node.right, running_sum, sums)
		
		
		
		
		
		
# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self

class TestProgram(unittest.TestCase):
	def test_case(self):
		tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10])
        # self.assertEqual(branchSums(tree), [15, 16, 18, 10, 11])

if __name__=='__main__':
	unittest.main()

