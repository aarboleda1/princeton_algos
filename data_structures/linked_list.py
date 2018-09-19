import unittest
from typing import Any, Optional


class Node:
    def __init__(self, val: Any, next: Optional[Any] = None) -> None:  # noqa
        self.val = val
        self.next = next

    def __call__(self):
        return [self.val, self.next]


class LinkedList:
    def __init__(self, val: Any) -> None:  # noqa
        self.first = Node(val)

    def addLast(self, val: Any) -> None:
        node = self.first
        while node.next is not None:
            node = node.next
        node.next = Node(val)

    def addFirst(self, val) -> None:
        old_first = self.first
        self.first = Node(val)
        self.first.next = old_first

    def contains(self, val) -> bool:
        node = self.first

        while node.next is not None:
            if node.val == val:
                return True
            node = node.next

        return False

    def pop(self) -> Any:
        node = self.first
        while node.next and node.next.next is not None:
            node = node.next
        node.next = None
        return False

    def getFirst(self) -> Any:
        return self.first.val

    def getLast(self):
        pass


class LinkedListTest(unittest.TestCase):
    def test_linked_list(self):
        linked_list = LinkedList(1)
        linked_list.addLast(2)
        linked_list.addLast(3)
        linked_list.addLast(4)

        self.assertTrue(
            linked_list.contains(2) is True
            and linked_list.contains(9) is False)

        # remove last item from the list
        linked_list.pop()
        self.assertTrue(linked_list.contains(4) is False)

        linked_list.addFirst(0)
        self.assertEqual(linked_list.getFirst(), 0, "Not first!")


if __name__ == '__main__':
    unittest.main()
