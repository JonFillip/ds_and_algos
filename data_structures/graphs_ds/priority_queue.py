import unittest


class PriorityQueue:
    def __init__(self):
        self.heap_list = [(0, 0)]  # Zero is the non-value in the heap list as
        # the
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
        if pos * 2 > self.current_size:
            return -1
        else:
            if (pos * 2) + 1 > self.current_size:
                return pos * 2
            elif self.heap_list[pos * 2] < self.heap_list[pos * 2 + 1]:
                return pos * 2
            else:
                return pos * 2 + 1

    def del_min(self):
        """Returns and removes the minimum value from the heap list."""
        front_val = self.heap_list[1][1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.percolate_down(1)
        return front_val

    def build_heap(self, sample_list):
        self.current_size = len(sample_list)
        self.heap_list = [(0, 0)]
        for item in sample_list:
            self.heap_list.append(item)
        pos = len(sample_list) // 2
        while pos > 0:
            self.percolate_down(1)
            pos -= 1

    def is_empty(self):
        """Checks if the queue is empty and returns a boolean"""
        if self.current_size == 0:
            return True
        else:
            return False

    def decrease_key(self, value, amount):
        """Reduces the min heap value by a specified amount."""
        done = False
        pos = 1
        the_key = 0
        while not done and pos <= self.current_size:
            if self.heap_list[pos][1] == value:
                done = True
                the_key = pos
            else:
                pos += 1
        if the_key > 0:
            self.heap_list[the_key] = (amount, self.heap_list[the_key][1])
            self.percolate_up(the_key)

    def __contains__(self, vertex):
        for pair in self.heap_list:
            if pair[1] == vertex:
                return True
        return False


class TestPriorityHeap(unittest.TestCase):
    def setUp(self):
        self.the_heap = PriorityQueue()
        self.the_heap.insert((2, 'Bowl'))
        self.the_heap.insert((3, 'Eggs'))
        self.the_heap.insert((1, 'flour'))
        self.the_heap.insert((4, 'Mix'))
        self.the_heap.insert((6, 'Fry'))
        self.the_heap.insert((8, 'serve'))

    def test_insert(self):
        assert self.the_heap.current_size == 6

    def test_del_min(self):
        assert self.the_heap.del_min() == 'flour'
        assert self.the_heap.del_min() == 'serve'

    def test_decrease_key(self):
        self.the_heap.decrease_key("Eggs", 1)
        assert self.the_heap.del_min() == "Eggs"


if __name__ == "__main__":
    unittest.main()
