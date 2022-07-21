# Height Balanced Tree
# https://www.algoexpert.io/questions/height-balanced-binary-tree

import unittest

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
def heightBalancedBinaryTree(tree):
    _, isBalanced = getHeightAndBalanced(tree)
    return isBalanced

def getHeightAndBalanced(node):
    if node is None:
        return -1, True
    L_height, L_balanced = getHeightAndBalanced(node.left)
    R_height, R_balanced = getHeightAndBalanced(node.right)
    node_height = max(L_height, R_height) + 1
    isBalanced = abs(L_height-R_height) <= 1 and L_balanced and R_balanced
    return node_height, isBalanced

######################################################################3

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        tree = BinaryTree(1)
        tree.left = BinaryTree(2)
        tree.right = BinaryTree(3)
        tree.left.left = BinaryTree(4)
        tree.left.right = BinaryTree(5)
        tree.right.right = BinaryTree(6)
        tree.left.right.left = BinaryTree(7)
        tree.left.right.right = BinaryTree(8)
        actual = heightBalancedBinaryTree(tree)
        self.assertEqual(actual, True)

if __name__=='__main__':
	unittest.main()
