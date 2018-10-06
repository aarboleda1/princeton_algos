"""
**Insertion Sort**

Time Complexity: O(N) ^ 2

Invariants:
  - Entries to the left of pointer are never changed and are in ascending order
  - No entry to the right of "i" smaller than any entry to the left of pointer

  Runs in linear time for partially sorted and sorted arrays
"""


def insertion_sort(arr):
    for i, num in arr:
        for j in range(len(arr) - 1, -1, -1):
            if num < arr[j]:
                exch(arr, i, j)
    return arr


def exch(arr, i, j):
    val = arr[i]
    arr[i] = arr[j]
    arr[j] = val
