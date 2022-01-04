# Find Closest Value in BST
# https://www.algoexpert.io/questions/Find%20Closest%20Value%20In%20BST

import unittest

def findClosestValueInBst(node, target, closest_val=float('inf')):
	if node is None:
		return closest_val
	
	if abs(target-closest_val) > abs(target-node.value):
		closest_val = node.value
	
	if node.value < target:
		return findClosestValueInBst(node.right, target, closest_val)
	elif node.value > target:
		return findClosestValueInBst(node.left, target, closest_val)
	else:
		return target

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BST(10)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.right = BST(5)
        root.right = BST(15)
        root.right.left = BST(13)
        root.right.left.right = BST(14)
        root.right.right = BST(22)

        expected = 13
        actual = findClosestValueInBst(root, 12)

        self.assertEqual(expected, actual)

if __name__=='__main__':
	unittest.main()
