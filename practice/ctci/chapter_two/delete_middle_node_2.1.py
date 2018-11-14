#!/usr/bin/env python3

"""Implement an algorithm to delete a node in a singly linked list, given only
access to that node
"""



"""SOLUTION
Solution is to copy data from node.next to current node and then
delete next node
"""


class Node:
    def __init__(self, val: int) -> None:
        self.next = None
        self.val = val

def del_middle_node(node: Node) -> None:
    if node is None or node.next is None:
        return
    next = node.next
    node.val = next.val
    node.next = next.next
