class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        """Checks if a queue is empty and returns a boolean values."""
        return self.items == []

    def enqueue(self, item):
        """Adds an item to the queue."""
        self.items.insert(0, item)

    def dequeue(self):
        """Removes the earliest values from the queue."""
        return self.items.pop()

    def size(self):
        """Returns the size or length of the queue"""
        return len(self.items)
