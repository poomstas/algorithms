# Remove Kth Node from End
# https://www.algoexpert.io/questions/Remove%20Kth%20Node%20From%20End


def removeKthNodeFromEnd(head, k):
    currentNode = head
    targetNode = head
    nodeCount = 1

    while nodeCount != k + 1:
        nodeCount += 1
        currentNode = currentNode.next

    if currentNode is None:
        head.value = head.next.value
        head.next = head.next.next
        return

    while currentNode.next is not None:
        currentNode = currentNode.next
        targetNode = targetNode.next

    targetNode.next = targetNode.next.next


#######################################################################

import unittest

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self

    def getNodesInArray(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = LinkedList(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])
        expected = LinkedList(0).addMany([1, 2, 3, 4, 5, 7, 8, 9])
        removeKthNodeFromEnd(test, 4)
        self.assertEqual(test.getNodesInArray(), expected.getNodesInArray())


if __name__ == "__main__":
    unittest.main()
