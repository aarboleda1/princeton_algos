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
        self.curr_size = 0

    def add(self, val: int):
        """Adds an object to this heap."""
        self.arr.append(val)
        # bubble up
        self._swim(len(self.arr) - 1)
        self.curr_size += 1

    def get(self):
        """Returns the priority element"""

    def peek(self) -> int:
        """Returns the element on top of heap but don't remove it."""
        return self.arr[1]

    def pop(self) -> int:
        """Returns the element on top of heap and remove it."""
        val = self.arr[1]
        self.arr.pop(1)
        self._sink()
        return val

    def get_min_child(self, idx: int) -> int:
        if self.arr[idx * 2] < self.arr[idx * 2 + 1]:
            return idx * 2
        else:
            return idx * 2 + 1

    def _sink(self) -> None:
        """Move down"""
        idx = 1
        while idx * 2 <= len(self.arr):
            min_idx = self.get_min_child(idx)
            if self.arr[min_idx] > self.arr[idx]:
                tmp = self.arr[min_idx]
                self.arr[min_idx] = self.arr[idx]
                self.arr[idx] = tmp
            idx = min_idx

    def _swim(self, idx: int) -> None:
        """For a max binary heap, bubble up until in correct place in array"""
        while idx > 1 and self.arr[idx] > self.arr[math.floor(idx / 2)]:
            self._exch(math.floor(idx / 2), idx)
            idx = math.floor(idx / 2)

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
        max_heap.add(7)
        self.assertEqual(max_heap.peek(), 7)

    def test_pop(self):
        max_heap = MaxBinaryHeap()
        max_heap.add(1)
        max_heap.add(2)
        max_heap.add(5)
        max_heap.add(7)
        self.assertEqual(max_heap.pop(), 7)
        self.assertListEqual(max_heap.arr, [None, 5, 2, 1])


if __name__ == '__main__':
    unittest.main()
