class Deque:
    """Structure for Deque."""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        """Checks to see if the deque is empty and returns a boolean values."""
        return self.items == []

    def addRear(self, item):
        """Adds a values to the rear of the deque."""
        self.items.insert(0, item)

    def addFront(self, item):
        """Adds a values to the start/front of the deque"""
        self.items.append(item)

    def removeFront(self):
        """Removes the item at the front of the deque."""
        return self.items.pop()

    def removeRear(self):
        """Removes the item at the rear of the deque."""
        return self.items.pop(0)

    def size(self):
        return len(self.items)
