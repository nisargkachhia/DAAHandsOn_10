class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._add_recursive(self.root, value)

    def _add_recursive(self, node, value):
        if value < node.value:
            if not node.left:
                node.left = TreeNode(value)
            else:
                self._add_recursive(node.left, value)
        else:
            if not node.right:
                node.right = TreeNode(value)
            else:
                self._add_recursive(node.right, value)

    def find(self, value):
        return self._find_recursive(self.root, value)

    def _find_recursive(self, node, value):
        if not node or node.value == value:
            return node
        elif value < node.value:
            return self._find_recursive(node.left, value)
        return self._find_recursive(node.right, value)

    def delete(self, value):
        self.root, _ = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if not node:
            return node, False
        if value < node.value:
            node.left, deleted = self._delete_recursive(node.left, value)
            return node, deleted
        elif value > node.value:
            node.right, deleted = self._delete_recursive(node.right, value)
            return node, deleted

        if not node.left:
            return node.right, True
        elif not node.right:
            return node.left, True

        min_larger_node = self._get_min(node.right)
        node.value = min_larger_node.value
        node.right, _ = self._delete_recursive(node.right, min_larger_node.value)
        return node, True

    def _get_min(self, node):
        while node.left:
            node = node.left
        return node

    def inorder_traversal(self):
        return self._inorder_recursive(self.root, [])

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)
        return result
