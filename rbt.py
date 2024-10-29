class RBTNode:
    def __init__(self, value, color="red"):
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.NIL_LEAF = RBTNode(value=None, color="black")  # Sentinel NIL leaf
        self.root = self.NIL_LEAF

    def add(self, value):
        new_node = RBTNode(value)
        new_node.left = new_node.right = self.NIL_LEAF
        self._insert(new_node)

    def _insert(self, new_node):
        parent, node = None, self.root
        while node != self.NIL_LEAF:
            parent = node
            if new_node.value < node.value:
                node = node.left
            else:
                node = node.right
        new_node.parent = parent

        if not parent:
            self.root = new_node
            new_node.color = "black"
        elif new_node.value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

        self._balance_insert(new_node)

    def _balance_insert(self, node):
        while node != self.root and node.parent.color == "red":
            parent = node.parent
            grandparent = parent.parent
            if parent == grandparent.left:
                uncle = grandparent.right
                if uncle.color == "red":
                    parent.color = uncle.color = "black"
                    grandparent.color = "red"
                    node = grandparent
                else:
                    if node == parent.right:
                        node = parent
                        self._rotate_left(node)
                    node.parent.color = "black"
                    grandparent.color = "red"
                    self._rotate_right(grandparent)
            else:
                uncle = grandparent.left
                if uncle.color == "red":
                    parent.color = uncle.color = "black"
                    grandparent.color = "red"
                    node = grandparent
                else:
                    if node == parent.left:
                        node = parent
                        self._rotate_right(node)
                    node.parent.color = "black"
                    grandparent.color = "red"
                    self._rotate_left(grandparent)
        self.root.color = "black"

    def _rotate_left(self, node):
        right_child = node.right
        node.right = right_child.left
        if right_child.left != self.NIL_LEAF:
            right_child.left.parent = node
        right_child.parent = node.parent
        if not node.parent:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child

    def _rotate_right(self, node):
        left_child = node.left
        node.left = left_child.right
        if left_child.right != self.NIL_LEAF:
            left_child.right.parent = node
        left_child.parent = node.parent
        if not node.parent:
            self.root = left_child
        elif node == node.parent.left:
            node.parent.left = left_child
        else:
            node.parent.right = left_child
        left_child.right = node
        node.parent = left_child

    def delete(self, value):
        node_to_delete = self._find_node(value)
        if node_to_delete:
            self._delete_node(node_to_delete)
        else:
            print(f"{value} not found in the Red-Black Tree.")

    def _delete_node(self, node):
        original_color = node.color
        if node.left == self.NIL_LEAF:
            replacement = node.right
            self._transplant(node, node.right)
        elif node.right == self.NIL_LEAF:
            replacement = node.left
            self._transplant(node, node.left)
        else:
            successor = self._get_min(node.right)
            original_color = successor.color
            replacement = successor.right
            if successor.parent == node:
                replacement.parent = successor
            else:
                self._transplant(successor, successor.right)
                successor.right = node.right
                successor.right.parent = successor
            self._transplant(node, successor)
            successor.left = node.left
            successor.left.parent = successor
            successor.color = node.color
        if original_color == "black":
            self._balance_delete(replacement)

    def _balance_delete(self, node):
        while node != self.root and node.color == "black":
            if node == node.parent.left:
                sibling = node.parent.right
                if sibling.color == "red":
                    sibling.color = "black"
                    node.parent.color = "red"
                    self._rotate_left(node.parent)
                    sibling = node.parent.right
                if sibling.left.color == "black" and sibling.right.color == "black":
                    sibling.color = "red"
                    node = node.parent
                else:
                    if sibling.right.color == "black":
                        sibling.left.color = "black"
                        sibling.color = "red"
                        self._rotate_right(sibling)
                        sibling = node.parent.right
                    sibling.color = node.parent.color
                    node.parent.color = "black"
                    sibling.right.color = "black"
                    self._rotate_left(node.parent)
                    node = self.root
            else:
                sibling = node.parent.left
                if sibling.color == "red":
                    sibling.color = "black"
                    node.parent.color = "red"
                    self._rotate_right(node.parent)
                    sibling = node.parent.left
                if sibling.left.color == "black" and sibling.right.color == "black":
                    sibling.color = "red"
                    node = node.parent
                else:
                    if sibling.left.color == "black":
                        sibling.right.color = "black"
                        sibling.color = "red"
                        self._rotate_left(sibling)
                        sibling = node.parent.left
                    sibling.color = node.parent.color
                    node.parent.color = "black"
                    sibling.left.color = "black"
                    self._rotate_right(node.parent)
                    node = self.root
        node.color = "black"

    def _transplant(self, u, v):
        if not u.parent:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _get_min(self, node):
        while node.left != self.NIL_LEAF:
            node = node.left
        return node

    def _find_node(self, value):
        current = self.root
        while current != self.NIL_LEAF:
            if value == current.value:
                return current
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return None

    def inorder_traversal(self):
        return self._inorder_recursive(self.root, [])

    def _inorder_recursive(self, node, result):
        if node != self.NIL_LEAF:
            self._inorder_recursive(node.left, result)
            if node.value is not None:
                result.append(node.value)
            self._inorder_recursive(node.right, result)
        return result
