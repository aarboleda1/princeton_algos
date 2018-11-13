#!/usr/bin/python3

from typing import List, Iterable
import unittest

"""
Question: Given an iterator of iterators, implement an interleaving iterator
In object-oriented programming, the iterator pattern is a design pattern in
which an iterator is used to traverse a container and access the container's
elements. The iterator pattern decouples algorithms from containers; in some
cases, algorithms are necessarily container-specific and thus cannot be
decoupled. This code snippet illustrates:

https://tinyurl.com/ycsxqmpa


Key details to keep in mind:
- How to determine that all iterators are exhausted
- Updating indices properly when modifying the underlying data-structure
- Going back to the start of the list of iterators after looping once
"""

class HasNextIterator:
    """Wrapper class so that we have hasNext in python"""
    def __init__(self, it):
        self._it = iter(it)
        self._next = None

    def __iter__(self):
        return self

    def has_next(self):
        if self._next:
            return True
        try:
            self._next = next(self._it)
            return True
        except StopIteration:
            return False

    def next_(self):
        if self._next:
            ret = self._next
            self._next = None
            return ret
        elif self.has_next():
            return self.next_()
        else:
            raise StopIteration()
"""
Solution 1:
Use a stack and delete from the stack if self.iterlist[i].hasNext() returns false

Alternatively, we can also just find the first iterable where hasNext() returns
true because deleting from a list is linear time complexity. For large inputs,
memory would be hurting though
"""

"""Solution 2: OPTIMIZED USING QUEUE
By using a queue data structure - we always pop from the front and call next()
on the current_iter. If hasNext() returns true for the current exception,
then add it to the back of the queue to be processed later
"""


class IF:
    def __init__(self, iterlist: List[HasNextIterator]):
        self.iterlist = iterlist
        self.len = len(iterlist)
        self.idx = 0

    def _next(self):
        current_iter = self.iterlist[self.idx]
        val = current_iter.next_() # noqa

        if not current_iter.has_next():
            self.iterlist.pop(self.idx)

        self.idx += 1
        if self.idx >= len(self.iterlist):
            self.idx = 0
        return val

    def hasNext(self) -> bool:
        return len(self.iterlist) > 0

# OPTIMIZED USING A QUEUE
class IFUsingQueue:
    def __init__(self, iterlist: List[HasNextIterator]):
        self.iterlist = iterlist
        self.len = len(iterlist)
        self.idx = 0

    def _next(self):
        curr_iter = self.iterlist.pop(0)
        ret = curr_iter.next_()
        if curr_iter.has_next():
            self.iterlist.append(curr_iter)
        return ret

    def hasNext(self) -> bool:
        return len(self.iterlist) > 0


class IterableTest(unittest.TestCase):
    def test_iter(self):
        # Input keys (use only 'a' through 'z' and lower case)

        it = IF([
            HasNextIterator([1, 2, 3]),
            HasNextIterator([4, 5, 6]),
            HasNextIterator([7, 8])
        ])
        self.assertEqual(it._next(), 1)
        self.assertEqual(it._next(), 4)
        self.assertEqual(it._next(), 7)
        my_it = IF([
            HasNextIterator([1, 2, 3]),
            HasNextIterator([4]),
        ])
        self.assertEqual(my_it._next(), 1)
        self.assertEqual(my_it._next(), 4)
        self.assertEqual(my_it._next(), 2)
        self.assertTrue(my_it.hasNext())
        self.assertEqual(my_it._next(), 3)
        self.assertFalse(my_it.hasNext())

    def test_iter_using_queue(self):
        it = IFUsingQueue([
            HasNextIterator([1, 2, 3]),
            HasNextIterator([4, 5, 6]),
            HasNextIterator([7, 8])
        ])
        self.assertEqual(it._next(), 1)
        self.assertEqual(it._next(), 4)
        self.assertEqual(it._next(), 7)
        my_it = IFUsingQueue([
            HasNextIterator([1, 2, 3]),
            HasNextIterator([4]),
        ])
        self.assertEqual(my_it._next(), 1)
        self.assertEqual(my_it._next(), 4)
        self.assertEqual(my_it._next(), 2)
        self.assertTrue(my_it.hasNext())
        self.assertEqual(my_it._next(), 3)
        self.assertFalse(my_it.hasNext())

if __name__ == '__main__':
    unittest.main()
