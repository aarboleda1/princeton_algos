#!/usr/bin/env python3
from typing import Any
"""
Return Kth to Last: Implement an algorithm to find the kth to last element of
a singly linked list.
"""


"""
My solution

1. Send a runner down the linked list to find the length, we'll call it p1 to
len
2. Iterate thru the linked list once again using p1, we know that if
len - p1 == k, we have found the kth to last

"""

def kth_to_last(node: Any, k: int) -> None:
    if node is None or node.next is None:
        return None

    len = 0
    curr = node
    i = 0
    while curr is not None:
        len += 1
        curr = curr.next

    curr = node
    while curr is not None:
        if len - i == k:
            return curr
        i += 1
        curr = curr.next

"""Solution from the book
Use 2 pointers
"""

def kth_to_last_alt(head: Any, k: int) -> None:
    p1 = head
    p2 = head
    for i in range(k):
        if p1 is None:
            return None
        p1 = p1.next
