#!/usr/bin/env python3

from typing import Any, Optional
import unittest


class Node:
    def __init__(self, val: Optional[int] = None) -> None:
        self.left = None
        self.right = None
        self.val = val


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

MIN_VAL = -100000000
# MY VERSION
def check_balanced(node: Node) -> bool:
    return _check_balanced(node) != MIN_VAL


def _check_balanced(node: Optional[Node]) -> int:
    if node is None:
        return 0

    left_height = _check_balanced(node.left) + 1
    right_height = _check_balanced(node.right) + 1

    if abs(left_height - right_height) > 1:
        return MIN_VAL

    return max(left_height, right_height)


def check_height(root: Optional[Node]) -> int:
    if root is None:
        return -1
    left_height = check_height(root.left)
    right_height = check_height(root.right)

    if left_height == MIN_VAL or right_height == MIN_VAL:
        return MIN_VAL

    if abs(left_height - right_height) > 1:
        return MIN_VAL
    else:
        return max(left_height, right_height) + 1


def is_balanced(root: Node) -> bool:
    return check_height(root) != MIN_VAL

class CheckBalancedTestCase(unittest.TestCase):
    def test_paths_with_sum(self):
        tree = Tree()
        tree.insert(4)
        tree.insert(1)
        tree.insert(2)
        tree.insert(5)
        tree.insert(6)
        self.assertTrue(is_balanced(tree.getRoot()))
        self.assertTrue(check_balanced(tree.getRoot()))


if __name__ == "__main__":
    unittest.main()
