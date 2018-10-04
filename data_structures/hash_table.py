#!/usr/bin/python3

from typing import Any, List
"""Hash Table with separate chaining

Uses a linked list for indexes in the array

Linear Probing
Hash: Map key to integer i between 0 and M - 1
Insert: Once you have hash index, put at arr[i], if free, if not free, try
i + 1, i + 2, i + 3
Search: Search at arr[i], if not there, try i + 1, i + 2, etc...,
    if you ever hit an empty array index, you have a search miss because if it
    were there, it would have already been inserted

The easiest way to implement delete is to find and remove the key–value pair
and then to reinsert all of the key–value pairs in the same cluster that appear
after the deleted key–value pair. If the hash table doesn't get too full, the
expected number of key–value pairs to reinsert will be a small constant.

An alternative is to flag the deleted linear-probing table entry so that it is
skipped over during a search but is used for an insertion. If there are too many
flagged entries, create a new hash table and rehash all key–value pairs.
"""


def hash(key: Any) -> int:
    return 0


class Node:
    def __init__(self, key: Any, val: Any, next: Any) -> None:
        self.key = key
        self.val = val
        self.next = next


class HashTableSeparateChaining:
    def __init__(self) -> None:
        self.list: List[Any] = []

    def get(self, key: Any) -> Any:
        idx = hash(key)
        node = self.list[idx]
        val = None
        while node is not None:
            if node.key == key:
                val = node.val
                break
            node = node.next
        return val
