#!/usr/bin/env python3

import unittest
from typing import List, Any, Union


class DynamicArray:
    """Dynamic array, implemented with a ring buffer
    (use a statically sized array underneath the hood)
    """

    def __init__(self, size) -> None:  # noqa
        self.size = size
        self.ptr = 0
        self.list: List[Any] = [None] * self.size

    def push(self, val: Union[str, int, None]) -> None:
        self.list[self.ptr] = val
        self.ptr += 1
        if self.ptr == self.size:
            other_list = [None] * self.size
            self.list = [*self.list, *other_list]
            self.size *= 2

    def pop(self) -> Union[str, int, None]:
        """Resize if 1/4th of the current array size
        """
        if self.ptr == 0:
            return "Cannot pop from an empty list!"

        val = self.list[self.ptr]
        self.list[self.ptr] = None
        self.ptr -= 1
        if self.ptr / self.size == .25:
            curr_vals = self.list[0:self.ptr + 1]
            curr_size = self.size
            self.list = [*curr_vals, *[None] * int(self.size / 2)]
            self.size = round(curr_size / 2)

        return val

    def getSize(self) -> int:
        return len(self.list)


class DynamicArrayTest(unittest.TestCase):
    def test_dynamic_array(self):
        size = 3
        dynamic_array = DynamicArray(size)
        self.assertEqual(len(dynamic_array.list), size)
        dynamic_array.push(1)
        dynamic_array.push(2)
        dynamic_array.push(3)
        self.assertEqual(dynamic_array.getSize(), size * 2,
                         "list did not double!")

    def test_dynamic_array_pop(self):
        size = 8
        dynamic_array = DynamicArray(size)
        self.assertEqual(len(dynamic_array.list), size)
        dynamic_array.push(1)
        dynamic_array.push(2)
        dynamic_array.push(3)
        dynamic_array.pop()
        dynamic_array.pop()

        self.assertEqual(dynamic_array.getSize(), round(size / 2),
                         "Should be {size} divided by 2")


if __name__ == '__main__':
    unittest.main()
