from typing import Any, Optional, Union


class Node:
    def __init__(
        self,
        val: Any,  # noqa
        count: int,
        left: Optional[Node] = None,  # noqa
        right: Optional[Node] = None,  # noqa
    ) -> None:  # noqa
        self.val = val
        self.left = left
        self.right = right
        self.count = count


class BST:
    def __init__(self, root: Optional[Node] = None) -> None:  # noqa
        self.root = root

    def get(self, key: Any) -> Union[Node, None]:
        x = self.root
        while x is not None:
            if x.val < key:
                x = x.left  # noqa
            elif x.val > key:
                x = x.right  # noqa
            else:
                return x
        return None

    # Two cases we must cover
    # 1 - key in tree, reset value
    # 2 - key not in tree, add new node
    def put(self, val: Any) -> None:
        self.root = self._put(self.root, val)

    def _put(self, node: Optional[Node], val: Any) -> Node:
        if node is None:
            return Node(val, 1)
        # Insert left if current val is less than the current node processing
        if val < node.val:
            node.left = self._put(node.left, val)  # noqa
        if val > node.val:
            node.right = self._put(node.right, val)  # noqa
        else:
            node.val = val
        self.count = 1 + self.size(node.left) + self.size(node.right)
        return Node(val, 1)

    def size(self, node: Optional[Node]) -> int:
        if node is None:
            return 0
        return node.count

    def get_min(self) -> Optional[Node]:
        x = self.root
        while x is not None and x.left is not None:
            x = x.left
        return x

    def get_max(self) -> Optional[Node]:
        x = self.root
        while x is not None and x.right is not None:
            x = x.right
        return x

    def floor(self, val: Any) -> Optional[Node]:
        """Given a value, find the node with the next greatest val
        Case 1: [k is the val at the root]
            The floor is k
        Case 2: [k is less than val at the root]
            The floor is in the left subtree
        Case 3: [k is greater than the val at the root]
            The floor if k is in the right subtree IF there is ANY val <= k in
            in the right subtree, otherwise it is the val in the root.
        """
        return self._floor(self.root, val)

    def _floor(self, node: Optional[Node], val: Any) -> Union[Node, None]:
        if node is None:
            return None
        # case 1
        if node is not None and val == node.val:
            return node

        # case 2
        if node is not None and val < node.val:
            return self._floor(node.left, val)

        # case 3
        if node is not None:
            maybe_floor = self._floor(node.right, val)
            # return root if there is no element in right sub subtree
            # that is greater than val
            if maybe_floor is None:
                return node
            else:
                return maybe_floor

        return None
