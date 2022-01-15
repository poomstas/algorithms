# Node Depths
# https://www.algoexpert.io/questions/Node%20Depths

import unittest

def nodeDepths(node, depth=0):
    if node is None:
        return 0

    return depth + \
        nodeDepths(node.left, depth+1) + \
        nodeDepths(node.right, depth+1)

#######################################################################

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.left.left = BinaryTree(4)
        root.left.left.left = BinaryTree(8)
        root.left.left.right = BinaryTree(9)
        root.left.right = BinaryTree(5)
        root.right = BinaryTree(3)
        root.right.left = BinaryTree(6)
        root.right.right = BinaryTree(7)
        actual = nodeDepths(root)
        self.assertEqual(actual, 16)

if __name__=='__main__':
	unittest.main()
