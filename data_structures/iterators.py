#!/usr/bin/python3

"""
Q: What is an iterator?
A: A data structure that has a method that returns an Iterator

An iterator is a class that has the methods

hasNext() and next()

https://techdevguide.withgoogle.com/resources/former-coding-interview-question-flatten-an-iterator-of-iterators/#code-challenge
https://en.wikipedia.org/wiki/Iterator_pattern
"""

from typing import List


class StackIterator:
    def __init__(self):
        self.stack: List[int] = []
        self.i = len(self.stack)

    def has_next(self):
        return self.i > 0

    def next(self):
        self.i -= 1
        return self.stack[self.i]
