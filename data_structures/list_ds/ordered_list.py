from data_structures.list_ds.node_class import Node


class OrderedList:
    """Simulation of an ordered list and methods."""

    def __init__(self):
        self.head = None

    def isEmpty(self):
        """Checks if the list is empty and returns a boolean value."""
        current = self.head
        return current is None

    def length(self):
        """Returns the number of items in the list."""
        current = self.head
        count = 0
        while current is not None:
            current = current.getNext()
            count += 1

        return count

    def add(self, item):
        """Adds an item in the head of the list or node."""
        current = self.head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.getData() > item:
                stop = True

            else:
                previous = current
                current = current.getNext()

        entr = Node(item)
        if previous is None:
            entr.setNext(self.head)
            self.head = entr
        else:
            entr.setNext(current)
            previous.setNext(entr)

    def search(self, item):
        """Searches for th e specified item and returns a boolean value if
        the item is in the list."""
        current = self.head
        found = False
        stop = False
        while current is not None and not found and not stop:
            if current.getData() == item:
                found = True
            elif current.getData() > item:
                stop = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        """Traverse the list to search for the specified item and removes the
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
