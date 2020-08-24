from data_structures.list_ds.node_class import Node


class UnorderedList:
    def __init__(self):
        """Assuming the start of a list is empty."""
        self.head = None

    def isEmpty(self):
        """Returns a boolean value if the head of the  list is a reference to
        None"""
        return self.head is None

    def add(self, item):
        """Add an item to the list."""
        entr = Node(item)
        entr.setNext(self.head)
        self.head = entr

    def length(self) -> int:  # Uses Linked List Traversal technique
        """Counts the number of items or node in a linked list"""
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()

        return count

    def search(self, item):  # Uses Linked List Traversal technique
        """Searches a list for an item and returns a boolean value indicating
        whether or not the item is present in the list."""
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getData()

        return found

    def remove(self, item):
        """Traverse the list to search for a specified item and removes the
        item."""
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def index(self, item):
        """Searches a list for the specified item and returns the item
        position or index."""
        current = self.head
        found = False
        position = 0
        while current is not None and found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                position += 1

        if not found:
            raise ValueError("Value not present in the list.")
        return position

    def pop_idx(self, index):
        """Removes and returns the last item in the list."""
        if index >= self.length():
            raise IndexError("ERROR: Pop Index, Index is out of range!")
        current_idx = 0
        current = self.head
        found = False
        while current is not None and not found:
            previous = current
            current = current.getNext()
            if current_idx == index:
                previous.setNext(current.getNext())
            current_idx += 1

    def get(self, index):
        """Returns the item in the specified index."""
        if index >= self.length():
            raise IndexError("GET: Get index out of range!")
        current_idx = 0
        current = self.head
        found = False
        while current is not None and not found:
            current = current.getNext()
            if current_idx == index:
                return current.getData()
            current_idx += 1

    def display(self):
        """Displays all the items in the list."""
        items = []
        current = self.head
        while current.getNext() is not None:
            current = current.getNext()
            items.append(current.getData())
        return items
