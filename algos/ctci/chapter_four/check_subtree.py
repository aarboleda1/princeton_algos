#!/usr/bin/env python3

from typing import Any, Optional, List
import unittest

"""
Check Subtree: T1 and T2 are two very large binary trees, with T1 much bigger
than T2. Create an algorithm to determine if T2 is a subtree of T1.

A tree T2 is a subtree of T1 if there exists a node n in T1 such that the
subtree of n is identical to T2. That is, if you cut off the tree at node n,
the two trees would be identical. Hints: #4, #7 7, #78, #37, #37
"""

"""
Initial algorithm
- DFS thru T1, If you find a Tnode that is == to T2.root, then do a dfs both,
return false the first time you don't see anything

    -- this can be improved though, because runtime is O(N^2)
Simple Approach: We know that in order traversal does not give us a unique ordering
We also know that pre order traversal gives us the tree from left to right,
which would be unique, but the only thing is Null Pointers. Whenever we encounter a
null pointer (i.e. where root is None) we can just append "X" or some random value
to the stringbuilder class. O(N + M) where N and M is # of nodes in t1 and t2

Another way: Use a string to accumulate and do a pre-order traversal of the tree

Accumulate two strings of the trees. If t1.indexOf(t2) != -1 then we know that
t1 is a subtree of
"""

class Tree:
    def __init__(self):
        self.rightoot = None

    def getRoot(self):
        return self.rightoot

    def insert(self, val):
        if self.rightoot is None:
            self.rightoot = Node(val)
        else:
            self._insert(val, self.rightoot)

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


class Node:
    def __init__(self, val: Optional[str] = None) -> None:
        self.left = None
        self.right = None
        self.val = val


class StringBuilder:
    def __init__(self) -> None:
        self.list: List[Any] = []

    def append(self, val: str) -> None:
        self.list.append(val)

    def get_result(self) -> str:
        return "".join(self.list)


# SIMPLE APPROACH
def check_subtree(t1: Node, t2: Node) -> bool:
    s1 = StringBuilder()
    s2 = StringBuilder()
    get_str_ordering(t1, s1)
    get_str_ordering(t2, s2)

    return s2.get_result().find(s1.get_result()) != -1


def get_str_ordering(root: Optional[Node], str_builder: StringBuilder) -> None:
    if root is None:
        str_builder.append("X")
        return

    str_builder.append(root.val) # noqa
    get_str_ordering(root.left, str_builder) # noqa
    get_str_ordering(root.right, str_builder) # noqa


# ALTERNATIVE APPROACH
def _check_subtree(t1: Node, t2: Node) -> bool:
    if t2 is None:
        return True
    return is_sub_tree(t1, t2)


def is_sub_tree(r1: Node, r2: Node) -> bool:
    if r1 is None:
        return False
    if r1.val == r2.val and trees_match(r1, r2):
        return True

    return is_sub_tree(r1.left, r2.left) or is_sub_tree(r1.right, r2.right)  # noqa


def trees_match(r1: Node, r2: Node) -> bool:
    if r1 is None and r2 is None:
        return True
    elif r1 is None or r2 is None:
        return False
    elif r1.val != r2.val:
        return False
    else:
        ## both sides need to match
        return trees_match(r1.left, r2.left) and trees_match(r1.right, r2.right)  # noqa
