# Validate BST
# https://www.algoexpert.io/questions/Validate%20BST

def validateBst(node, left_max=float('inf'), right_min=-float('inf')):
    if node is None:
        return True

    if node.left is not None and node.left.value >= node.value:
        return False
    
    if node.right is not None and node.value > node.right.value:
        return False

    left_valid = validateBst(node.left, node.value, right_min)
    right_valid = validateBst(node.right, left_max, node.value)

    return left_valid and right_valid
	
#######################################################################

import unittest

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
        self.assertEqual(validateBst(root), True)

if __name__=='__main__':
	unittest.main()
