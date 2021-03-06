#!/usr/bin/env python3

"""
https://hackernoon.com/bst-sequences-in-python-c072c0e9b19f
https://stackoverflow.com/questions/21211701/given-a-bst-and-its-root-print-all-sequences-of-nodes-which-give-rise-to-the-sa/24398114#24398114
http://www.yujinc.com/4-9-bst-sequences-cci/
The main idea for generating sequence is that root must come before all its
children.


1. Create a function allSequences which generates all possible lists
 - Base case where root is null, return [[]]
 - Otherwise, recurisvely call allSequences and get the left and right
 sequences of left and right subtree
2. weaveLists Function
e.g.
    arr1: [1, 2, 3]
    arr2: [4, 5, 6]

    Think of the sub problems
    - Prepend a 1 to all weaves of [2, 3] and [4, 5, 6]
    - Prepend a 4 to all weaves of [1, 2, 3] and [5, 6]
When arr1 or arr2 are empty, add the remainder to prefix arr and store result

"""
from typing import List, Any, Optional
import copy


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


def allSequences(node: Optional[Node]) -> List[Any]:
    # this is the final list of lists we want to output
    results: List[List[Any]] = []
    # termination, append [] so that results will not be empty
    # and the nested for loop will still execute since
    # leftSeq == [[]] and rightSeq == [[]] in termination
    if not node:
        results.append([])
        return results

    # prefix will always be root of subtree
    prefix = []
    prefix.append(node.val)

    # then represent the left and right subtrees
    leftSeq = [getSequences(node.left)]
    rightSeq = [getSequences(node.right)]
    # nested for loop and call weaveLists on each list in
    # leftSeq and rightSeq, which are list of lists
    # and each represents results of each subtree
    for left in leftSeq:
        for right in rightSeq:
            # make weaved an empty list,
            # which is results in weaveList
            weaved: List[Any] = []
            weaveLists(left, right, weaved, prefix)
            # weaved is list of lists generated by left[] and right[]
            # add weaved list of lists to final
            # results list of lists
            results += weaved
    return results


def getSequences(node: Optional[Node]) -> List[int]:
    """Get sequences of an array, must use in-order DFS to preserve proper
    ordering
    """
    if node is None:
        return []

    left = getSequences(node.left)
    right = getSequences(node.right)
    return left + [node.val] + right  # noqa


def weaveLists(first, second, results, prefix):
    # if first or second is an empty list
    if not first or not second:
        # ensuring that result is a CLONE and not a reference to prefix
        result = copy.deepcopy(prefix)
        # add result to first or/ and second lists
        if first:
            result += first
        if second:
            result += second
        # append the weaved list which is result, to results
        results.append(result)
        return
    # this would be the method as described in the textbook
    # first, remove and store first element of first[]
    headFirst = first.pop(0)
    # append to prefix
    prefix.append(headFirst)

    ### add recursive call to operate on first[]
    weaveLists(first, second, results, prefix)
    # exit when first[] is empty
    # reset prefix for second recursive call below by removing last element
    # IMPT to modify in-place
    del prefix[-1]
    # reset first[] for second recursive call below by adding back first element
    # IMPT to modify in-place
    first.insert(0, headFirst)
    # do the same thing on the second[]
    headSecond = second.pop(0)
    prefix.append(headSecond)
    ### add recursive call to operate on first[] and second[]
    weaveLists(first, second, results, prefix)
    del prefix[-1]
    second.insert(0, headSecond)



if __name__ == "__main__":
    tree = Tree()

    tree.insert(4)
    tree.insert(1)
    tree.insert(2)
    tree.insert(5)
    tree.insert(3)
    tree.insert(6)
    allSeq = allSequences(tree.getRoot())
    for each in allSeq:
        print(each)
