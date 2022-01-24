# Sum of Linked Lists
# https://www.algoexpert.io/questions/Sum%20of%20Linked%20Lists


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    valOne = readLinkedListValue(linkedListOne)
    valTwo = readLinkedListValue(linkedListTwo)
    final_value = valOne + valTwo
    return createOutputLinkedList(final_value)


def readLinkedListValue(linkedList):
    value = 0
    multiplier = 1
    current_node = linkedList
    while current_node is not None:
        value += current_node.value * multiplier
        multiplier *= 10
        current_node = current_node.next
    return value


def createOutputLinkedList(value):
    values = [int(value) for value in reversed(list(str(value)))]
    linked_list = LinkedList(values[0])
    current_node = linked_list
    for val in values[1:]:
        current_node.next = LinkedList(val)
        current_node = current_node.next
    return linked_list


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


def getNodesInArray(output):
    nodes = []
    current = output
    while current is not None:
        nodes.append(current.value)
        current = current.next
    return nodes


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        ll1 = LinkedList(2).addMany([4, 7, 1])
        ll2 = LinkedList(9).addMany([4, 5])
        expected = LinkedList(1).addMany([9, 2, 2])
        actual = sumOfLinkedLists(ll1, ll2)
        self.assertEqual(getNodesInArray(actual), getNodesInArray(expected))


if __name__ == "__main__":
    unittest.main()
