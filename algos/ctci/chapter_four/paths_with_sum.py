#!/usr/bin/env python3

from typing import List, Any, Optional
import copy
import unittest
"""
You are given a binary tree in which each node contains an integer
value. Design an algorithm to count the number of paths that sum to a given
value. The path does not need to start at the root or at a leaf, but it must
go downwards.


Brute Force: Traverse thru tree. For each node traverse "look" for a potential
Should work, but the time complexity is O(N Log N) for a balanced tree and
will be O(N^2) for an unbalanced binary tree

Optimized: There is a lot of repeated work here. We're looking at subpaths of the
tree. Basically the same as contiguous subsequences problem where there are 2
ways you can find a new path
1. if the running sum is == target
i.e. [3, 2, -1] and target is 4 or
2. if we have [8, 2, 1, -1, 2] where it's the subsequence is [2, 1, -1, 2]

In this case we can just keep track of the running sum at each node and store that
value such that the currrent running sum

(curr_sum - target) == some value we have computed before. If it does exist,
we can use a hash table to keep track of number of occurences. And then add it
to our result



"""


class Node:
    def __init__(self, val: Optional[int] = None) -> None:
        self.left = None
        self.right = None
        self.val = val


class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(val, self.root)

    def _insert(self, val, node):
        if val < node.val:
            if node.left is not None:
                self._insert(val, node.left)
            else:
                node.left = Node(val)
        else:
            if node.right is not None:
                self._insert(val, node.right)
            else:
                node.right = Node(val)


def paths_with_sum(node, target):
    return _paths_with_sum(node, target, 0, {}) # return count


def _paths_with_sum(node, target, running_sum, sum_map):
    if node is None:
        return 0

    running_sum += node.val
    sum = running_sum - target
    key = str(sum)

    res = 0
    if key in sum_map:
        res = sum_map[key]
    elif running_sum == target:
        res += 1

    str_running_sum = str(running_sum)

    if str_running_sum in sum_map:
        sum_map.setdefault(str_running_sum, 1)
    else:
        sum_map[str_running_sum] = 1

    res += _paths_with_sum(node.left, target, running_sum, sum_map)
    res += _paths_with_sum(node.right, target, running_sum, sum_map)

    # set back state to before
    sum_map[str_running_sum] -= 1
    return res


class PathsWithSumTestCase(unittest.TestCase):
    def test_paths_with_sum(self):
        tree = Tree()
        tree.insert(4)
        tree.insert(1)
        tree.insert(2)
        tree.insert(5)
        tree.insert(3)
        tree.insert(6)
        self.assertTrue(paths_with_sum(tree.getRoot(), 6) == 2)


if __name__ == "__main__":
    unittest.main()
