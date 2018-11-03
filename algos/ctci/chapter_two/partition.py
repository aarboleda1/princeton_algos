#!/usr/bin/env python3

import unittest


class Node:
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next


class DoubleList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, node_value):
        current_node = self.head

        while current_node is not None:
            if current_node.data == node_value:
                # if it's not the first element
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                else:
                    # otherwise we have no prev (it's None), head is the next
                    # one, and prev becomes None
                    self.head = current_node.next
                    current_node.next.prev = None

            current_node = current_node.next

    def contains(self, val) -> bool:
        node = self.head
        if node is None:
            return False

        while node is not None:
            if node.data == val:
                return True
            node = node.next


class LinkedListTest(unittest.TestCase):
    def test_linked_list(self):
        linked_list = DoubleList()
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(4)

        self.assertTrue(
            linked_list.contains(2) is True
            and linked_list.contains(9) is False)

        # remove last item from the list
        linked_list.remove(4)
        self.assertTrue(linked_list.contains(4) is False)

        linked_list.addFirst(0)
        self.assertEqual(linked_list.getFirst(), 0, "Not first!")


if __name__ == '__main__':
    unittest.main()
