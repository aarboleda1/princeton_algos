#!/usr/bin/python3

from typing import Any, List
import random
import unittest

"""Quicksort

Not stable by default

Basic Plan:
    Partition the array so that, for some j
    - Entry arr[j] is in place
    - No entry to the left of j is larger than j
    - No entry to the right of j is less than j
    - Sort each piece recursively

Implementation Details to note:
- It partitions in place. You could use an extra array but it takes up extra space
- One of the advantages of how quicksort is is that it doesn't take up any extra space as
compared to merge sort
- Terminating the loop. You have to make sure the pointers stay in bounds
- *Duplicates:
"""


def swap(arr: List[Any], i: int, j: int) -> None:
    val = arr[i]
    arr[i] = arr[j]
    arr[j] = val


def quick_sort_randomized(alist: List[int], lo: int, hi: int) -> List[int]:
    """Generates Random Pivot, swaps pivot with
    end element and calls the partition function
    """
    if lo < hi:
        random_partition = partition_random(alist, lo, hi)
        quick_sort_randomized(alist, lo, random_partition - 1)
        quick_sort_randomized(alist, random_partition + 1, hi)
    return alist


def partition_random(alist: List[int], lo: int, hi: int) -> int:
    rand_idx = random.randint(lo, hi)
    swap(alist, rand_idx, hi)
    return partition(alist, lo, hi)


def quick_sort(arr: List[int], lo: int, hi: int) -> List[int]:  # noqa
    if lo < hi:
        j = partition(arr, lo, hi)
        quick_sort(arr, lo, j - 1)
        quick_sort(arr, j + 1, hi)
    return arr


# Notice low - 1 and i + 1, This is done for list index so that index
# does not go out of bounds


def partition(arr: List[Any], lo: int, hi: int) -> int:
    pivot = arr[lo]
    i = lo + 1
    j = hi
    while True:
        # move i pointer until we find an element out of place
        while i <= j and arr[i] < pivot:
            i = i + 1

        # move j pointer until we find an element out of place
        while i <= j and arr[j] > pivot:
            j = j - 1

        if i >= j:
            break
        swap(arr, i, j)

    swap(arr, lo, j)
    return j


def _partition(arr, low, high):
    i = low - 1  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:

            # increment index of smaller element
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # final and important step, we can place pivot
    # in proper place in array
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


a = quick_sort([8, 2, 1, 0, 9], 0, 4)
print(a)


class QuickSortTest(unittest.TestCase):
    def test_sort(self):
        arr = [8, 1, 2, 5, 0]
        sorted = quick_sort(arr, 0, len(arr) - 1)
        self.assertListEqual(sorted, [0, 1, 2, 5, 8], "Incorrect!")

    def test_one_other_way_sort(self):
        arr = [8, 1, 2, 5, 0]
        sorted = quick_sort(arr, 0, len(arr) - 1)
        self.assertListEqual(sorted, [0, 1, 2, 5, 8], "Incorrect!")

    def test_one_other_way_sort_(self):
        arr = [8, 1, 2, 5, 0]
        sorted = quick_sort_randomized(arr, 0, len(arr) - 1)
        self.assertListEqual(sorted, [0, 1, 2, 5, 8], "Incorrect!")


if __name__ == "__main__":
    unittest.main()
