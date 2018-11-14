"""
First Common Ancestor: Design an algorithm and write code to find the first
common ancestor of two nodes in a binary tree. Avoid storing additinoal
nodes in a data structure. NOTE: This is not necessarily a binary tree

Case where we do not have links to parent
"""























"""In this case we can check traverse down the tree where p and q are on the
same side.

Case 1. If p and q are on the left side, branch and search for a FCA down the
left (do same for right)

Case 2. If they are not on the same side, then the current root is the FCA

Runs in O(N) time
"""


def covers():
    """see first_common_ancestor.py"""
    pass


def common_ancestor(root, p, q):
    if not covers(root, p) or not covers(root, q):
        return None
    return common_ancestor_helper(root, p, q)


def common_ancestor_helper(root, p, q):
    if root is None:
        return None

    isPOnLeft = covers(root.left, p)
    isQonLeft = covers(root.left, q)

    # They are on different sides of trees, so this is FCA
    if isPOnLeft != isQonLeft:
        return root

    root_to_discover = root.left if (isPOnLeft is True and isQonLeft) else root.right
    return common_ancestor(root_to_discover, p, q)

"""Solution 2: OPTIMIZED
 My initial approach was correct, just had a hard time distinguishing

 Recurse thru the tree w a function called common_ancestor(root, p, q) and the
 function will return teh values as follows

 - Return p, if root's subtree includes p
 - Return q, if root's subtree includes q
 - Returns null if neither q or p in subtree
 - Else return common ancestor of p and q
"""

# def common_ancestor_optimized():
