#!/usr/bin/env python3
"""Implement a method to perform basic string compression using the counts of
repeated characters. For example, the string aabccccaaa would become a2b1c5a3.
If the "compressed" string would not become smaller than the original string,
your method should return the original string. You can assume the string has
only uppercase and lowercase letters (a-z).
"""
import unittest
from typing import List


# basic solution NOT GOOD!
"""Runtime is O(p + k2), where p is the size of the original string and k is the
number of character sequences.
"""


class StringBuilder:
    def __init__(self) -> None:
        self.list: List[str] = []
        self.length = len(self.list)

    def append(self, val: str) -> None:
        self.list.append(val)

    def get_val(self) -> str:
        return ""


def compress_string_BAD(string: str) -> str:
    compressed = ""
    count_consecutive = 0
    for i in range(len(string)):
        count_consecutive += 1
        if i + 1 >= len(string) or string[i] != string[i + 1]:
            compressed += string[i]
            compressed += str(count_consecutive)
            count_consecutive = 0
    return compressed if len(compressed) < len(string) else string


def compress_string_GOOD(string: str) -> str:
    compressed = StringBuilder()
    count_consecutive = 0
    for i in range(len(string)):
        count_consecutive += 1
        if i + 1 >= len(string) or string[i] != string[i + 1]:
            compressed.append(string[i])
            compressed.append(str(count_consecutive))
            count_consecutive = 0
    return compressed.get_val() if compressed.length < len(string) else string


class StringCompressionTest(unittest.TestCase):
    def test_string_compression(self):
        string = "aabccccaaa"
        self.assertEqual(compress_string_BAD(string), "a2b1c4a3")


if __name__ == '__main__':
    unittest.main()
