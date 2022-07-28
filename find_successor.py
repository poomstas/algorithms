# Find Successor
# https://www.algoexpert.io/questions/find-successor

import unittest

class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def findSuccessor(tree, target_node):
    nodes = getNodesInOrderDFS(tree)
    nodes.append(None)
    for i, node in enumerate(nodes[:-1]):
        if node is target_node:
            break
    return nodes[i+1]

def getNodesInOrderDFS(node, output=[]):
    if node is None:
        return output
    output = getNodesInOrderDFS(node.left, output)
    output.append(node)
    output = getNodesInOrderDFS(node.right, output)
    return output

######################################################################3

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.left.parent = root
        root.right = BinaryTree(3)
        root.right.parent = root
        root.left.left = BinaryTree(4)
        root.left.left.parent = root.left
        root.left.right = BinaryTree(5)
        root.left.right.parent = root.left
        root.left.left.left = BinaryTree(6)
        root.left.left.left.parent = root.left.left
        node = root.left.right
        expected = root
        actual = findSuccessor(root, node)
        self.assertEqual(actual, expected)

if __name__=='__main__':
	unittest.main()
