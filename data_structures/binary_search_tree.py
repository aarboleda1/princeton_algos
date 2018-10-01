from typing import Any, Optional, Union


class Node:
    def __init__(
        self,
        key: Any,  # noqa
        count: int,
        left: Optional[Node] = None,  # noqa
        right: Optional[Node] = None,  # noqa
    ) -> None:  # noqa
        self.key = key
        self.left = left
        self.right = right
        self.count = count


class BST:
    def __init__(self, root: Optional[Node] = None) -> None:  # noqa
        self.root = root

    def get(self, key: Any) -> Union[Node, None]:
        x = self.root
        while x is not None:
            if x.key < key:
                x = x.left  # noqa
            elif x.key > key:
                x = x.right  # noqa
            else:
                return x
        return None

    # Two cases we must cover
    # 1 - key in tree, reset value
    # 2 - key not in tree, add new node
    def put(self, key: Any) -> None:
        self.root = self._put(self.root, key)

    def _put(self, node: Optional[Node], key: Any) -> Node:
        if node is None:
            return Node(key, 1)
        # Insert left if current key is less than the current node processing
        if key < node.key:
            node.left = self._put(node.left, key)  # noqa
        if key > node.key:
            node.right = self._put(node.right, key)  # noqa
        else:
            node.key = key
        self.count = 1 + self.size(node.left) + self.size(node.right)
        return Node(key, 1)

    def size(self, node: Optional[Node]) -> int:
        if node is None:
            return 0
        return node.count

    def get_min(self, root: Optional[Node]) -> Optional[Node]:
        x = self.root if root is None else root
        while x is not None and x.left is not None:
            x = x.left
        return x

    def get_max(self) -> Optional[Node]:
        x = self.root
        while x is not None and x.right is not None:
            x = x.right
        return x

    def floor(self, key: Any) -> Optional[Node]:
        """Given a value, find the node with the next greatest key
        Case 1: [k is the key at the root]
            The floor is k
        Case 2: [k is less than key at the root]
            The floor is in the left subtree
        Case 3: [k is greater than the key at the root]
            The floor if k is in the right subtree IF there is ANY key <= k in
            in the right subtree, otherwise it is the key in the root.
        """
        return self._floor(self.root, key)

    def _floor(self, node: Optional[Node], key: Any) -> Union[Node, None]:
        if node is None:
            return None
        # case 1
        if node is not None and key == node.key:
            return node

        # case 2
        if node is not None and key < node.key:
            return self._floor(node.left, key)

        # case 3
        if node is not None:
            maybe_floor = self._floor(node.right, key)
            # return root if there is no element in right sub subtree
            # that is greater than key
            if maybe_floor is None:
                return node
            else:
                return maybe_floor

        return None

        def del_min(self, node: Optional[Node]) -> Optional[Node]:
            if node is not None and node.left is None:
                return node.right

            # recurse
            node.left = self.del_min(node.left)
            node.count = 1 + self.size(node.left) + self.size(node.right)
            return node

        def del_max(self, node: Optional[Node]) -> Optional[Node]:
            if node is not None and node.right is None:
                return node.right

            # recurse
            node.right = self.del_min(node.right)
            node.count = 1 + self.size(node.left) + self.size(node.right)
            return node

        def delete(self, key: Any) -> Optional[Node]:
            """Delete a node with value key
            Case 1:[1 child]
                Delete t by replacing parent link
            Case 2: [2 children]
                - Find the successor node of t
                - Find the minimum in nodes right subtree and delete it
                -
            """
            self.root = self._delete(self.root, key)

        def _delete(self, root: Optional[Node], key: Any) -> Optional[Node]:
            if root is None:
                return root

            # search left
            if key < root.key:
                root.left = self._delete(root.left, key)
            # search right
            elif key > root.key:
                root.left = self._delete(root.right, key)
            else:
                # node with only 1 child
                if root.left is None:
                    temp = root.right
                    root = None
                    return temp
                elif root.right is None:
                    temp = root.left
                    root = None
                    return temp

                # node with 2 children
                # get the in order successor (smallest in right tree)
                temp = self.get_min(root.right)
                root.key = temp.key

                # delete node of inorder successor
                root.right = self.del_min(root.right, node)

            return root
