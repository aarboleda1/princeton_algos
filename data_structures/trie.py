#!/usr/bin/env python3
"""A trie is a tree-like data structure whose nodes store the letters of an
alphabet. By structuring the nodes in a particular way, words and strings
can be retrieved from the structure by traversing down a branch path of the tree.
- Good article detailing basics of a trie
https://medium.com/basecs/trying-to-understand-tries-3ec6bede0014
Each trie has an empty root node, with links to other nodes - one for each
possible alphabetic value. For the english language, each node will have
26 child nodes

Root node is typically empty

*Deleting from a trie*
If we want to remove a key/value pair, we first find the node for that key,
and its value to null. Once the node has a value, check if its references are
null. If they are we can remove it, and repeat/work way back up the trie

*Hash Tables vs Tries*
They both use arrays under the hood but there are a few differences
- Tries don't require or need a hash function. Why? Because every key can be
represented in order (alphabetically) and is uniquely retrieveable since every
branch path to a string’s value will be unique to that key.
- Downside to tries - they can take up a lot of memory and space with null
pointers

*Big O Notation*
Creation:
- The worst-case runtime for creating a trie is a combination of m,
the length of the longest key in the trie, and n, the total number
of keys in the trie. Thus, the worst case runtime of creating a trie is O(mn)
Searching/inserting/deleting:
- Depends on the length of the word "a" and the total number of words O(a * m).

Deleting from a Trie:
-
"""
from typing import List, Any, Optional
import unittest


class TrieNode:
    def __init__(self, char: Optional[str] = None) -> None:
        self.children: List[Any] = [None] * 26
        self.char = char
        self.is_end_of_word = False

    def is_free(self) -> bool:
        for c in self.children:
            if c:
                return False
        return True

    def is_leaf(self) -> bool:
        return self.char is None

class Trie:
    def __init__(self) -> None:
        self.root = self.get_node()

    def search(self, key: str) -> bool:
        p = self.root
        if len(key) > 0:
            for char in key:
                idx = self._charToIndex(char)
                if p.children[idx] is None:
                    return False
                p = p.children[idx]
        return p is not None and p.is_end_of_word

    def insert(self, key: str) -> None:
        p = self.root
        if len(key) > 0:
            for char in key:
                idx = self._charToIndex(char)
                if p.children[idx] is None:
                    p.children[idx] = TrieNode(char)
                p = p.children[idx]
            p.is_end_of_word = True

    def delete_util(self, key: str, level: int, length: int,
                    node: TrieNode) -> bool:
        char = key[level]
        idx = self._charToIndex(char)
        if node.children[idx] is None:
            return False

        # base case
        if level == length:
            if node.char:
                node.char = None
            return node.is_free()
        else:
            if self.delete_util(key, level + 1, length, node.children[idx]):
                del node.children[idx]
                return not node.is_leaf() and node.is_free()

        return False

    def delete(self, key: str) -> None:
        """
        1. key is not in the tree
        2. delete something that is not end of word
        3. delete a key, but it has many children below. e.g. the trie
        has the word "absolute" but you need to delete abs
        """
        self.delete_util(key, 0, len(key), self.root)

    def get_node(self) -> TrieNode:
        return TrieNode()

    def _charToIndex(self, char: str) -> int:
        return ord(char) - ord('a')


#
#
# class TrieNode:
#     def __init__(self, value: Optional[str] = None) -> None:
#         # this is if your using lowercase english alphabet
#         # if it's larger you can use a dictionary to support more characters
#         self.children: List[Any] = [None] * 26
#         self.is_end_of_word = False
#         self.value = value
#
#     def is_free(self) -> bool:
#         """If node has no children then we can delete this node
#         """
#         for c in self.children:
#             if c:
#                 return False
#         return True
#
#     def is_leaf_node(self) -> bool:
#         """Leaf nodes have no children and no value"""
#         return self.value is not None
#
#
# class Trie:
#     def __init__(self) -> None:
#         self.root = self.get_node()
#
#     def insert(self, key: str) -> None:
#         pointer = self.root
#
#         for level in range(len(key)):
#             idx = self._charToIndex(key[level])
#             if not pointer.children[idx]:
#                 pointer.children[idx] = self.get_node()
#             pointer = pointer.children[idx]
#
#         # mark last node as leaf
#         pointer.is_end_of_word = True
#
#     def search(self, key: str) -> bool:
#         pCrawl = self.root
#
#         for level in range(len(key)):
#             idx = self._charToIndex(key[level])
#             if not pCrawl.children[idx]:
#                 return False
#             pCrawl = pCrawl.children[idx]
#
#         return pCrawl is not None and pCrawl.is_end_of_word
#
#     def delete_key(self, key: str) -> None:
#         if len(key) > 0:
#             self.delete_key_helper(key, self.root, 0, len(key))
#
#     def delete_key_helper(self, key: str, pNode: TrieNode, level: int,
#                           length: int) -> bool:
#         if pNode:
#             # base case
#             if level == length:
#                 # if it has a value we want to unmark it
#                 if pNode.value:
#                     pNode.value = None
#                 return pNode.is_free()
#             # recursive
#             else:
#                 index = self._charToIndex(key[level])
#                 if self.delete_key_helper(key, pNode.children[index],
#                                           level + 1, length):
#                     del pNode.children[index]
#                     return not pNode.is_leaf_node() and pNode.is_free()
#
#         return False
#
#     def get_node(self) -> TrieNode:
#         return TrieNode()
#
#     def _charToIndex(self, ch: str) -> int:
#         # private helper function
#         # Converts key current character into index
#         # use only 'a' through 'z' and lower case
#         return ord(ch) - ord('a')
#
#
class TrieTest(unittest.TestCase):
    def test_trie(self):
        # Input keys (use only 'a' through 'z' and lower case)
        keys = ["the", "a", "there", "anaswe", "any", "by", "their"]

        t = Trie()
        for key in keys:
            t.insert(key)
        self.assertTrue(t.search("the"))
        self.assertFalse(t.search("th"))
        self.assertTrue(t.search("any"))


if __name__ == '__main__':
    unittest.main()
