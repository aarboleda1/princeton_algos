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

Another way: Aggregate both trees into arrays. Use a sliding window algo for T1
"""


class Node:
    def __init__(self):
        self.left = None
        self.right = None


def get_nodes(node, target, target_matches):
    """Returns a list of nodes that match with t2's root"""
    if node is None:
        return
    if node.val == target.val:
        target_matches.append(node)
    get_nodes(node.left)
    get_nodes(node.right)


def dfs(t1, t2):
    if t1.val != t2.val:
        return False

    return (dfs(t1.left, t2.left) and dfs(t2.right, t2.right)) is not False


def check_subtree(t1, t2):
    nodes = get_nodes(t1, t2.root, [])
    for node in nodes:
        if dfs(node, t2) is False:
            continue
        elif dfs(node, t2) is True:
            return True
