# BST Traversal
# https://www.algoexpert.io/questions/BST%20Traversal

import unittest

# All O(N) time | O(N) space
def inOrderTraverse(node, array):
	if node is None:
		return
	inOrderTraverse(node.left, array)
	array.append(node.value)
	inOrderTraverse(node.right, array)
	return array

def preOrderTraverse(node, array):
    if node is None:
        return
    array.append(node.value)
    preOrderTraverse(node.left, array)
    preOrderTraverse(node.right, array)
    return array

def postOrderTraverse(node, array):
    if node is None:
        return
    postOrderTraverse(node.left, array)
    postOrderTraverse(node.right, array)
    array.append(node.value)
    return array

#######################################################################

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
        root.right.right = BST(22)

        inOrder = [1, 2, 5, 5, 10, 15, 22]
        preOrder = [10, 5, 2, 1, 5, 15, 22]
        postOrder = [1, 2, 5, 5, 22, 15, 10]

        self.assertEqual(inOrderTraverse(root, []), inOrder)
        self.assertEqual(preOrderTraverse(root, []), preOrder)
        self.assertEqual(postOrderTraverse(root, []), postOrder)

if __name__=='__main__':
	unittest.main()