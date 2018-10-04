#!/usr/bin/python3

import unittest
from typing import Any, List


class Queue:

    """Queue with stacks only"""
    def __init__(self) -> None:
        self.s1: List[Any] = []
        self.s2: List[Any] = []

    def enqueue(self, val: Any) -> None:
        self.s1.append(val)

    def dequeue(self) -> Any:

        while len(self.s1) != 0:
            self.s2.append(self.s1.pop())

        val = self.s2.pop()

        while len(self.s2) != 0:
            self.s1.append(self.s2.pop())
        return val


class QueueTest(unittest.TestCase):
    def test_enqueue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        val = queue.dequeue()
        self.assertEqual(val, 1, 'Not equal!')
        val = queue.dequeue()
        self.assertEquals(val, 2, 'Not equal!')


if __name__ == '__main__':
    unittest.main()
