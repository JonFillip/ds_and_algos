class BinaryTree:
    """Implementation of a binary tree using nodes and references."""
    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child is None:  # In case there is no existing node in
            # the left child
            self.left_child = BinaryTree(new_node)
        else:  # In case there is an already existing node in the left child.
            # The new left node pushes the existing node down the tree.
            left_branch = BinaryTree(new_node)
            left_branch.left_child = self.left_child
            self.left_child = left_branch

    def insert_right(self, new_node):
        if self.right_child is None:  # In case there is no existing node in
            # the right child.
            self.right_child = BinaryTree(new_node)
        else:  # In case there is an already existing node in the right child.
            # The new right node pushes the existing node down the tree.
            right_branch = BinaryTree(new_node)
            right_branch.right_child = self.right_child
            self.right_child = right_branch

    def preorder(self):
        """Traverses the tree recursively in a preorder manner."""
        print(self.key)
        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()

    def inorder(self):
        """Traverses the tree recursively in an inorder manner"""
        if self.left_child:
            self.left_child.inorder()
        print(self.key)
        if self.right_child:
            self.right_child.inorder()

    def postorder(self):
        """Traverses the tree recursively in a post-orderly manner"""
        if self.left_child:
            self.left_child.postorder()
        if self.right_child:
            self.right_child.postorder()
        print(self.key)

    def set_root_value(self, value):
        """Sets an object in the root node."""
        self.key = value

    def get_left_child(self):
        """Returns the values or left subtree."""
        return self.left_child

    def get_right_child(self):
        """Returns the values in the right subtree."""
        return self.right_child

    def get_root(self):
        """Returns the value in the root node."""
        return self.key
