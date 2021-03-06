class BinaryHeap:
    def __init__(self):
        self.heap_list = [0]  # Zero is the non-value in the heap list as the
        # first value in the list should start from index 1
        self.current_size = 0  # Current size of the heap tree

    def percolate_up(self, pos):
        """This method handles the swapping of values smaller than their
        parents are percolated upwards the heap following the min_heap
        approach."""
        while pos // 2 > 0:
            if self.heap_list[pos] < self.heap_list[pos // 2]:
                self.heap_list[pos // 2], self.heap_list[pos] = \
                    self.heap_list[pos], self.heap_list[pos // 2]

            pos //= 2

    def insert(self, value):
        """Inserts a new value in the heap"""
        self.heap_list.append(value)
        self.current_size += 1
        self.percolate_up(self.current_size)

    def percolate_down(self, pos):
        """When deleting a value from the heap this method handles the
        maintains the heap structure property and the heap order property by
        pushing down the new root node in the tree to its proper position."""
        while (pos * 2) >= self.current_size:
            min_c = self.min_child(pos)
            if self.heap_list[pos] > self.heap_list[min_c]:
                self.heap_list[pos], self.heap_list[min_c] = self.heap_list[
                                                                 min_c], \
                                                             self.heap_list[pos]
            pos = min_c

    def min_child(self, pos):
        """Returns the minimum key value in the heap."""
        if (pos * 2) + 1 > self.current_size:
            return pos * 2
        elif self.heap_list[pos * 2] < self.heap_list[pos * 2 + 1]:
            return pos * 2
        else:
            return pos * 2 + 1

    def del_min(self):
        """Returns and removes the minimum value from the heap list."""
        front_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.percolate_down(1)
        return front_val

    def build_min_heap(self, sample_list):
        pos = len(sample_list) // 2
        self.current_size = len(sample_list)
        self.heap_list = [0] + sample_list[:]
        while pos > 0:
            self.percolate_down(1)
            pos -= 1

    def is_empty(self):
        """Checks if the queue is empty and returns a boolean"""
        if self.current_size == 0:
            return True
        else:
            return False

    def Print(self):
        """Print a formatted string representation of the heap."""
        for pos in range(1, (self.current_size // 2) + 1):
            print(f"PARENT NODE: {self.heap_list[pos]} "
                  f" LEFT CHILD: {self.heap_list[pos * 2]}"
                  f" RIGHT CHILD: {self.heap_list[pos * 2 + 1]}")


mini_heap = BinaryHeap()
a_list = [3, 56, 2, 10, 2, 8, 11]
for i in a_list:
    mini_heap.insert(i)
mini_heap.Print()
print(f"Minimum child is : {mini_heap.del_min()}")
