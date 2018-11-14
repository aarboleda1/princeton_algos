#!/usr/bin/env python3

"""Implement class MyQueue using only two stacks
"""
from typing import List
import unittest


class MyQueue:
    def __init__(self) -> None:
        self.newest: List[int] = []
        self.oldest: List[int] = []

    def peek(self) -> int:
        self.shift_stacks()
        return self.oldest[len(self.oldest) - 1]

    def enqueue(self, val: int) -> None:
        self.newest.append(val)

    def dequeue(self) -> int:
        if len(self.newest) == 0:
            self.shift_stacks()
        return self.oldest.pop()

    def shift_stacks(self) -> None:
        while self.newest:
            self.oldest.append(self.newest.pop())


"""
newest [5]
oldest [3]
"""
class MyQueueTest(unittest.TestCase):
    def test_linked_list(self):
        q = MyQueue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertTrue(q.peek() == 1)
        self.assertTrue(q.dequeue() == 1)
        q.enqueue(5)
        self.assertTrue(q.dequeue() == 2)


if __name__ == '__main__':
    unittest.main()
