class TreeNode:
    def __init__(self, key, value, left=None, right=None, parent=None,
                 balance=0):
        self.key = key
        self.payload = value
        self.left_child = left
        self.right_child = right
        self.parent = parent
        self.balance_factor = balance

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_parent(self):
        return not self.parent

    def is_leaf(self):
        return not (self.right_child or self.left_child)

    def possess_children(self):
        return self.right_child or self.left_child

    def possess_both_children(self):
        return self.right_child and self.left_child

    def replace_node_data(self, key, value, left_c, right_c):
        self.key = key
        self.payload = value
        self.left_child = left_c
        self.right_child = right_c
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self

    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.possess_children():
            if self.has_right_child():
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent
        else:
            if self.is_left_child():
                self.parent.left_child = self.right_child
            else:
                self.parent.right_child = self.right_child
            self.right_child.parent = self.parent

    def find_successor(self):
        succ = None
        if self.has_left_child():
            succ = self.right_child.find_min()
        else:
            if self.parent:
                self.parent.right_child = None
                succ = self.parent.find_successor()
                self.parent.right_child = self
        return succ

    def find_min(self):
        current = self
        while current.has_left_child():
            current = current.left_child
        return current

    def __iter__(self):
        if self:
            if self.has_left_child():
                for value in self.left_child:
                    yield value
            yield self.key
            if self.has_right_child():
                for value in self.right_child:
                    yield value
