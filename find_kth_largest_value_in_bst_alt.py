# Find Kth Largest Value in BST
# https://www.algoexpert.io/questions/Find%20Kth%20Largest%20Value%20In%20BST


# O(N) time | O(N) space
def findKthLargestValueInBst(tree, k):
    ordered_array = []
    collectValues(tree, ordered_array)
    return ordered_array[-k]


def collectValues(node, array=[]):
    if node is None:
        return
    collectValues(node.left, array)
    array.append(node.value)
    collectValues(node.right, array)


#######################################################################

import unittest


class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BST(15)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.left.right = BST(3)
        root.left.right = BST(5)
        root.right = BST(20)
        root.right.left = BST(17)
        root.right.right = BST(22)
        k = 3
        expected = 17
        actual = findKthLargestValueInBst(root, k)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
