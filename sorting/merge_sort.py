#!/usr/bin/python3

import unittest
"""Divide and Conquer Paradigm:

steps
- Divide array into 2 halves and then merge sorted halves

Stable: Yes
"""


def merge_sort(alist):

    print("Splitting ", alist)

    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1

        return alist

    print("Merging ", alist)


def _merge_sort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        left = alist[:mid]
        right = alist[mid:]
        return _merge(_merge_sort(left), _merge_sort(right))
    return alist


def _merge(left, right):
    res = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            res.append(left[left_idx])
            left_idx += 1
        else:
            res.append(right[right_idx])
            right_idx += 1
    # rest of letters
    while left_idx < len(left):
        res.append(left[left_idx])
        left_idx += 1

    while right_idx < len(right):
        res.append(right[right_idx])
        right_idx += 1

    return res


class MergeSortTest(unittest.TestCase):
    def test_sort(self):
        arr = [8, 1, 2, 5, 0]
        sorted = merge_sort(arr)
        self.assertListEqual(sorted, [0, 1, 2, 5, 8], 'Incorrect!')

    def test_other_way_sort(self):
        arr = [8, 1, 2, 5, 0]
        sorted = _merge_sort(arr)
        self.assertListEqual(sorted, [0, 1, 2, 5, 8], 'Incorrect!')


if __name__ == '__main__':
    unittest.main()
