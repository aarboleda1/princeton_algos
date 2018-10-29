#!/usr/bin/env python3
from typing import Optional



class Node:
    def __init__(self, val: Optional[int] = None) -> None:
        self.val = val
        self.left = None
        self.right = None


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
