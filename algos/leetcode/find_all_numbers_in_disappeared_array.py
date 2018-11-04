#!/usr/bin/env python3

"""
The basic idea is that we iterate through the input array and mark elements
as negative using nums[nums[i] -1] = -nums[nums[i]-1]. In this way all the
numbers that we have seen will be marked as negative. In the second iteration,
if a value is not marked as negative, it implies we have never seen that index
before, so just add it to the return list.
"""

"""
The idea here is to iterate thru the input array and mark:

nums[nums[i] - 1] = -nums[nums[i]-1]

i.e. the VALUE at that index - 1, make it negative

Now nums will be transformed to have negative numbers at indexes in which
the value exists. When you iterate a second time, if you see a postivie number
At that index, so you can just push i + 1 into the result array

A. Iterate thru array. For each number mark nums[nums[i] - 1] to be negative
B. Then iterate thru array, if you see a number larger than 0, append whatever
index it is at to result array
"""
from typing import List
import unittest


def find_all_numbers_not_in_array(alist: List[int]) -> List[int]:
    res = []
    if List is None:
        return []
    for n in alist:
        val = abs(n) - 1
        alist[val] = -val

    for n in alist:
        if n > 0:
            res.append(n)

    return res


class FindAllNumbersTest(unittest.TestCase):
    def find_all_numbers_not_in_array_test(self):
        a = [4, 3, 2, 7, 8, 2, 3, 1]
        res = find_all_numbers_not_in_array(a)
        self.assertListEqual(res, [5, 6])


if __name__ == "__main__":
    unittest.main()
