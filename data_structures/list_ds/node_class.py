class Node:
    """Creates the features and functionalities of a Linked list."""
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def getData(self):
        """Returns the initial values in the node."""
        return self.data

    def getNext(self):
        """Returns the next item in a node."""
        return self.next

    def setData(self, new_data):
        """Sets an item in a node's values field."""
        self.data = new_data

    def setNext(self, next_data):
        """Sets the values of the next node."""
        self.next = next_data
