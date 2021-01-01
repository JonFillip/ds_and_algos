from data_structures.binary_trees.tree_node import TreeNode


class BinarySearchTree(TreeNode):
    def __init__(self, key, value):
        self.root = None
        self.size = 0
        super().__init__(key, value, left=None, right=None, parent=None,
                         balance=0)

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def insert(self, key, value):
        if self.root:
            self._insert(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
        self.size += 1

    def _insert(self, key, value, current_node):
        if key < current_node.key:
            if current_node.has_left_child():
                self._insert(key, value, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, value,
                                                   parent=current_node)
        else:
            if current_node.has_right_child():
                self._insert(key, value, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, value,
                                                    parent=current_node)

    def __setitem__(self, key, value):
        self.insert(key, value)

    def get(self, key):
        if self.root:
            self._get(key, self.root)
            if self._get(key, self.root):
                return self._get(key, self.root).TreeNode.payload
            else:
                return None
        else:
            return None

    def _get(self, key, current_node):
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        elif key > current_node.key:
            return self._get(key, current_node.right_child)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            remove_node = self._get(key, self.root)
            if remove_node:
                self.remove(remove_node)
                self.size -= 1
            else:
                raise KeyError(f"Error, key {key} not in the tree.")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError(f"Error, key {key} not found in the tree.")

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, current_node):
        if current_node.is_leaf():
            if current_node == current_node.parent.left_child:
                current_node.parent.left_child = None
            else:
                current_node.parent.right_child = None
        elif current_node.possess_both_children():
            succ = current_node.find_successor()
            succ.splice_out()
            current_node.key = succ.key
            current_node.payload = succ.payload
        else:  # the node has only one child
            if current_node.has_left_child():
                if current_node.is_left_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                elif current_node.is_right_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.left_child
                else:
                    current_node.replace_node_data(
                        current_node.left_child.key,
                        current_node.left_child.payload,
                        current_node.left_child.left_child,
                        current_node.left_child.right_child
                    )

            else:
                if current_node.is_left_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.right_child
                elif current_node.is_right_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                else:
                    current_node.replace_node_data(
                        current_node.right_child.key,
                        current_node.right_child.payload,
                        current_node.right_child.left_child,
                        current_node.right_child.right_child
                    )


class AvlTree(BinarySearchTree):
    """Class for a balance tree."""
    # balance factor = height(left_subtree) - height(right_subtree)
    # if balance factor > 0, then the subtree is left heavy
    # if balance factor < 0, then the subtree is right heavy
    # balance factor has been set in the TreeNode class as 0

    def _insert(self, key, value, current_node):
        if key < current_node.key:
            if current_node.has_left_child():
                self._insert(key, value, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, value,
                                                   parent=current_node)
                self.update_balance(current_node.left_child)

        else:
            if current_node.has_right_child():
                self._insert(key, value, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, value,
                                                    parent=current_node)
                self.update_balance(current_node.right_child)

    def update_balance(self, node):
        if node.balance_factor > 1 or node.balance_factor < -1:
            self.rebalance(node)
            return
        if node.parent is not None:
            if node.is_left_child():
                node.parent.balance_factor += 1
            elif node.is_right_child():
                node.parent.balance_factor -= 1

            if node.parent.balance_factor != 0:
                self.update_balance(node.parent)

    def rotate_left(self, old_root):
        """Left rotation implementation"""
        new_root = old_root.right_child
        old_root.right_child = new_root.left_child
        if new_root.left_child is not None:
            new_root.left_child.parent = old_root
        new_root.parent = old_root.parent
        if old_root.is_parent():
            self.parent = new_root
        else:
            if old_root.is_left_child():
                old_root.parent.left_child = new_root
            else:
                old_root.parent.right_child = new_root
        new_root.left_child = old_root
        old_root.parent = new_root
        old_root.balance_factor = old_root.balance_factor + 1 - min(
            new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor + 1 + max(
            old_root.balance_factor, 0)

    def rotate_right(self, old_root):
        """Right rotation implementation"""
        new_root = old_root.left_child
        old_root.left_child = new_root.right_child
        if new_root.right_child is not None:
            new_root.right_child.parent = old_root
        new_root.parent = old_root.parent
        if old_root.is_parent():
            self.parent = new_root
        else:
            if old_root.is_right_child():
                old_root.parent.right_child = new_root
            else:
                old_root.parent.left_child = new_root
        new_root.right_child = old_root
        old_root.parent = new_root
        old_root.balance_factor = old_root.balance_factor + 1 - max(
            new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor + 1 + min(
            old_root.balance_factor, 0)

    def rebalance(self, node):
        if node.balance_factor < 0:  # If the subtree needs a left rotation.
            if node.TreeNode.right_child.balance_factor > 0:  # 1st check the
                # balance factor of the right child. If the right child is
                # left heavy then perform a right rotation on the right child
                # followed by the original left rotation
                self.rotate_right(node.TreeNode.right_child)
                self.rotate_left(node)
            else:
                self.rotate_left(node)
        elif node.balance_factor > 0:  # If the subtree needs a right rotation
            if node.TreeNode.left_child.balance_factor < 0:  # 1st check the
                # balance factor of the left child. If the left child is
                # right heavy then perform a left rotation ob the left child
                # followed by the original right rotation
                self.rotate_left(node.TreeNode.left_child)
                self.rotate_right(node)
            else:
                self.rotate_right(node)
