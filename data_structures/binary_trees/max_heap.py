class MaxBinaryHeap:
    """Implementation of a max heap"""

    def __init__(self):
        self.heap_list = [0]  # Zero is a non-value in the heap list as the
        # first value in the list should start from index 1
        self.current_size = 0  # Current size of the heap tree

    def percolate_up(self, pos):
        """
        Swaps values larger than their parents. Percolates upwards the heap
        following the max_heap approach.
        """
        while pos // 2 > 0:
            if self.heap_list[pos] > self.heap_list[pos // 2]:
                self.heap_list[pos // 2], self.heap_list[pos] = \
                    self.heap_list[pos], self.heap_list[pos // 2]
            pos //= 2

    def insert(self, value):
        """Inserts a new value into the heap."""
        self.heap_list.append(value)
        self.current_size += 1
        self.percolate_up(self.current_size)

    def percolate_down(self, pos):
        """After deleting a value from the heap the method maintains the heap
        property and the heap order property by pushing down the new root in
        the tree to its proper position."""
        while pos * 2 <= self.current_size:
            max_node = self.max_child(pos)
            if self.heap_list[pos] < self.heap_list[max_node]:
                self.heap_list[pos], self.heap_list[max_node] = \
                    self.heap_list[max_node], self.heap_list[pos]

            pos = max_node

    def max_child(self, pos):
        """Returns the maximum key value in the heap."""
        if (pos * 2) + 1 > self.current_size:  # Note that pos * 2 + 1;
            # represents the right child of the heap
            return (pos * 2) + 1
        elif self.heap_list[pos * 2] > self.heap_list[pos * 2 + 1]:
            return pos * 2  # Note: pos * 2 represents the left child

        else:
            return pos * 2 + 1

    def del_max(self):
        """Returns and removes the maximum value from the heap list"""
        front_value = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.percolate_up(1)
        return front_value

    def build_heap(self, a_list):
        pos = len(a_list) // 2
        self.current_size = len(a_list)
        self.heap_list = [0] + a_list[:]
        while pos > 0:
            self.percolate_up(1)
            pos += 1

    def Print(self):
        """Print a formatted string representation of the heap."""
        for pos in range(1, (self.current_size // 2) + 1):
            print(f"PARENT NODE: {self.heap_list[pos]} "
                  f" LEFT CHILD: {self.heap_list[pos * 2]}"
                  f" RIGHT CHILD: {self.heap_list[pos * 2 + 1]}")


max_heap = MaxBinaryHeap()
a_list = [3, 56, 2, 10, 2, 8, 11]
for i in a_list:
    max_heap.insert(i)
max_heap.Print()
print(f"Minimum child is : {max_heap.del_max()}")
