#!/usr/bin/env python3

"""
1.1 Implement an algorithm to dete3rmine if a string is unique. What if you
cannot use any additional data structures?

Solutions
1. Sort string using quick_sort, it's stable and and in place
"""


def quick_sort(s: str):
    pass


def is_unique(s: str) -> bool:
    sorted_str = quick_sort(s)
    for i in range(len(sorted_str)):
        if sorted_str[i] == sorted_str[i + 1]:
            return False
    return True

# Runs in O(N) time
