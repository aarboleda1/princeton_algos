"""
First Common Ancestor: Design an algorithm and write code to find the first
common ancestor of two nodes in a binary tree. Avoid storing additinoal
nodes in a data structure. NOTE: This is not necessarily a binary tree
"""























"""
Solution 1: Case where we have links to parents

The two nodes we'll, call them p and q

Traverse up the tree to find the first intersection

Few caveats. We need to first know the depth of each node. Once we know the
depth of both nodes, then move up the deeper node by the delta of depths

At this point, the two nodes will be at the same level of the tree

Now, we can move each node up by 1 until a parent matches
"""


def get_depth(node):
    depth = 0
    while node is not None:
        node = node.parent
        depth += 1
    return depth


def move_up(node, delta):
    while delta > 0 and node is not None:
        node = node.parent
        delta -= 1
    return node


def first_common_ancestor(p, q):
    """Args:
    Node {
        parent
        left
        right
    }
    p: Node
    q: Node
    """
    pDepth = get_depth(p)
    qDepth = get_depth(q)
    delta = pDepth - qDepth
    first = p if delta > 0 else q  # shallower node
    second = q if delta > 0 else p # deeper node
    second = move_up(second, abs(delta))

    while first != second and first is not None and second is not None:
        first = first.parent
        second = second.parent

    return None if (first is None or second is None) else first


"""
Solution 2: Case where we have links to parents
Similar to the first solution. We can traverse up p and check if any of the
nodes cover q. The first one that does is the FCA

Caveats - As we move from node x to it's parent, all nodes have been checked for
q. Therefore we only need to check the subtree of the sibling node for q
"""


def covers(root, node):
    if root is None:
        return False
    if root == node:
        return True
    return covers(root.left, node) or covers(root.right, node)


def get_sibling(node):
    if node is None or node.parent is None:
        return None
    parent = node.parent
    return parent.right if parent.right != node else parent.left


def FCA(root, p, q):
    # Check that both nodes are in the tree OR one node covers another
    if not covers(root, q) or not covers(root, p):
        return None
    elif covers(p, q):
        return p
    elif covers(q, p):
        return q

    parent = p.parent
    sibling = get_sibling(p)
    while not covers(sibling, q):
        sibling = get_sibling(parent)
        parent = parent.parent
    return parent
