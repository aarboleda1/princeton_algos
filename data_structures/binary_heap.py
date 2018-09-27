#!/usr/bin/env python3
import unittest

from typing import Any, List
import math
"""Constructs a Binary Heap
Key concepts:
- Height is always Log ^ 2 of N nodes in binary tree
- For a Max Binary heap:
    - Every element must be larger than its two children

"""


class MaxBinaryHeap:
    def __init__(self) -> None:
        self.arr: List[Any] = [None]

    def add(self, val: int):
        """Adds an object to this heap."""
        self.arr.append(val)
        # bubble up
        self._swim(len(self.arr) - 1)
        pass

    def get(self):
        """Returns the priority element"""

    def peek(self) -> int:
        """Returns the element on top of heap but don't remove it."""
        return self.arr[1]

    def pop(self):
        """Returns the element on top of heap and remove it."""

    def remove(self):
        """Removes priority Element"""

    def _sink(self, idx: int) -> None:
        """Move down"""
        pass

    def _swim(self, idx: int) -> None:
        """For a max binary heap, bubble up until in correct place in array"""
        parent_idx = math.floor(idx / 2)
        while idx > 1 and self.arr[idx] > self.arr[parent_idx]:
            self._exch(parent_idx, idx)
            idx = parent_idx

    def _exch(self, parent_idx: int, idx: int) -> None:
        temp = self.arr[idx]
        self.arr[idx] = self.arr[parent_idx]
        self.arr[parent_idx] = temp


class BinaryHeapTest(unittest.TestCase):
    def test_swim(self):
        max_heap = MaxBinaryHeap()
        max_heap.add(1)
        max_heap.add(2)
        max_heap.add(5)
        self.assertListEqual(max_heap.arr, [None, 5, 1, 2])

    def test_peek(self):
        max_heap = MaxBinaryHeap()
        max_heap.add(1)
        max_heap.add(2)
        max_heap.add(5)
        self.assertEqual(max_heap.peek(), 5)


if __name__ == '__main__':
    unittest.main()
