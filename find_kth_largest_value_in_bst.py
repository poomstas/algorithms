# Find Kth Largest Value in BST
# https://www.algoexpert.io/questions/Find%20Kth%20Largest%20Value%20In%20BST

# O(h + k) time | O(h) space - where h is the height of the BST, and k is the param.
class VisitData:
    """Class variable to keep track of the visit information."""

    def __init__(self, last_value, visit_count):
        self.last_value = last_value
        self.visit_count = visit_count


def findKthLargestValueInBst(tree, k):
    visitData = VisitData(None, 0)
    findKthLargest(tree, k, visitData)
    return visitData.last_value


def findKthLargest(node, k, visitData):
    if node is None or visitData.visit_count == k:
        return

    findKthLargest(node.right, k, visitData)

    if visitData.visit_count < k:
        visitData.visit_count += 1
        visitData.last_value = node.value
        findKthLargest(node.left, k, visitData)


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
