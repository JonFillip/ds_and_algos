"""The following code simulates a stack. LIFO operations"""


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        """This method checks if a stack is empty and returns a boolean value"""
        return self.items == []

    def push(self, item):
        """Adds a new value to the top of the stack at index 0"""
        self.items.append(item)

    def pop(self):
        """Pops or removes the item at index 0 in a stack"""
        return self.items.pop(0)

    def peek(self):
        """Returns the top item from the stack without modifying it"""
        return self.items[0]

    def size(self):
        """Returns the number of items in the stack"""
        return len(self.items)
