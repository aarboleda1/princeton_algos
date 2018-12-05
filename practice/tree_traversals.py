#!/usr/bin/env python3
from typing import Optional, List
import unittest

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


"""Preorder Traversal
1. Process node
2. Visit all nodes in left subtree
3. Visit all nodes in right subtree
"""
def pre_order(root: Optional[Node]) -> None:
    if root is None:
        return

    print(root.val)
    pre_order(root.left)
    pre_order(root.right)


"""Postorder Traversal
1. Visit all nodes in left subtree
2. Visit all nodes in right subtree
3. Process node
"""
def post_order(root: Optional[Node]) -> None:
    if root is None:
        return

    post_order(root.left)
    post_order(root.right)
    print(root.val)

"""Inorder Traversal
1. Visit all nodes in left subtree
2. Process node
3. Visit all nodes in right subtree
"""
def in_order(root: Optional[Node]) -> None:
    if root is None:
        return

    in_order(root.left)
    print(root.val)
    in_order(root.right)


"""Inorder Traversal
1. Visit all nodes in left subtree
2. Process node
3. Visit all nodes in right subtree
"""
def in_order_array(root: Optional[Node]) -> List[int]:
    if root is None:
        return []

    res = in_order_array(root.left)
    res += [root.val] # noqa
    res += in_order_array(root.right)
    return res

def pre_order_array(root: Optional[Node], res: List[int]) -> None:
    if root is None:
        return

    res += [root.val]  # noqa
    pre_order_array(root.left, res)
    pre_order_array(root.right, res)

def post_order_list(root: Optional[Node]) -> List[int]:
    if root is None:
        return []

    res = post_order_list(root.left)
    res += post_order_list(root.right)
    res += [root.val]  # noqa
    return res

def post_order_list_p(root: Optional[Node]) -> None:
    if root is None:
        return
    post_order_list_p(root.left)
    post_order_list_p(root.right)
    print(root.val)

def test_tree_pre_order():
    tree = Tree()
    tree.insert(5)
    tree.insert(2)
    tree.insert(1)
    tree.insert(10)
    tree.insert(9)
    post_order_list_p(tree.root)
    # self.assertListEqual(a, [5, 2, 1, 10, 9])
class TreeTraversaltest(unittest.TestCase):
    def test_tree_in_order(self):
        tree = Tree()
        tree.insert(5)
        tree.insert(2)
        tree.insert(1)
        tree.insert(10)
        tree.insert(9)
        self.assertListEqual(in_order_array(tree.root), [1, 2, 5, 9, 10])

    def test_tree_pre_order(self):
        tree = Tree()
        tree.insert(5)
        tree.insert(2)
        tree.insert(1)
        tree.insert(10)
        tree.insert(9)
        a = []
        pre_order_array(tree.root, a)
        self.assertListEqual(a, [5, 2, 1, 10, 9])

    def test_tree_post_order(self):
        tree = Tree()
        tree.insert(5)
        tree.insert(2)
        tree.insert(1)
        tree.insert(10)
        tree.insert(9)
        self.assertListEqual(post_order_list(tree.root), [1, 2, 9, 10, 5])



if __name__ == '__main__':
    unittest.main()
