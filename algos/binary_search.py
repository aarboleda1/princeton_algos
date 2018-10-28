#!/usr/bin/env python3
from typing import List
from math import floor
import unittest


def binary_search_recursive(alist: List[int], target: int) -> bool:
    return binary_search_recursive_helper(alist, 0, len(alist) - 1, target)


def binary_search_recursive_helper(
    alist: List[int], lo: int, hi: int, target: int
) -> bool:
    # catch errors first
    if lo > hi:
        return False

    mid = floor(lo + ((hi - lo) / 2))
    if alist[mid] == target:
        return True

    if alist[mid] > target:
        return binary_search_recursive_helper(alist, lo, mid - 1, target)
    else:
        return binary_search_recursive_helper(alist, mid + 1, hi, target)


def binary_search_iterative(alist: List[int], target: int) -> bool:
    lo = 0
    hi = len(alist) - 1

    while lo <= hi:
        mid = floor(lo + ((hi - lo) / 2))
        if alist[mid] == target:
            return True
        if alist[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return False



class BinarySearch(unittest.TestCase):
    def test_recursive(self):
        alist = [1, 3, 5, 9, 11]
        self.assertTrue(binary_search_recursive(alist, 5))
        self.assertTrue(binary_search_recursive(alist, 3))
        self.assertTrue(binary_search_recursive(alist, 9))
        self.assertTrue(binary_search_recursive(alist, 11))
        self.assertTrue(binary_search_recursive(alist, 1))
        self.assertFalse(binary_search_recursive(alist, 100))

    def test_iterative(self):
        alist = [1, 3, 5, 9, 11]
        self.assertTrue(binary_search_iterative(alist, 5))
        self.assertTrue(binary_search_iterative(alist, 3))
        self.assertTrue(binary_search_iterative(alist, 9))
        self.assertTrue(binary_search_iterative(alist, 11))
        self.assertTrue(binary_search_iterative(alist, 1))
        self.assertFalse(binary_search_iterative(alist, 100))

if __name__ == '__main__':
    unittest.main()
