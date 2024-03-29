# Binary Tree Diameter
# https://www.algoexpert.io/questions/Binary%20Tree%20Diameter

import unittest

# Perform a DFS while keeping track of key relevant components (diameter and height of the node)
# Get a practice on explaining how the algorithm works. That's more important than the coding part.

# O(N) time | O(H) space avg, O(N) max
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
class TreeInfo:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height


def binaryTreeDiameter(tree):
    return getTreeInfo(tree).diameter

def getTreeInfo(node):
    if node is None:
        return TreeInfo(0, 0)

    L = getTreeInfo(node.left)    # Left Subtree Info
    R = getTreeInfo(node.right)   # Right Subtree Info

    # Determine Current Node's Tree Diameter
    max_path_thru_node = L.height + R.height
    node_diameter = max(L.diameter, R.diameter, max_path_thru_node)

    # Determine Current Node's Tree Height
    node_height = max(L.height, R.height) + 1

    return TreeInfo(node_diameter, node_height)
	

######################################################################3

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BinaryTree(1)
        root.left = BinaryTree(3)
        root.left.left = BinaryTree(7)
        root.left.left.left = BinaryTree(8)
        root.left.left.left.left = BinaryTree(9)
        root.left.right = BinaryTree(4)
        root.left.right.right = BinaryTree(5)
        root.left.right.right.right = BinaryTree(6)
        root.right = BinaryTree(2)
        expected = 6
        actual = binaryTreeDiameter(root)
        self.assertEqual(actual, expected)

if __name__=='__main__':
	unittest.main()
