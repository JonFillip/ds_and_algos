from data_structures.queues_ds.queue import Queue

"""
This program simulates the game of hot potato using a FIFO principle. In real 
world players of the game pass around a item and when the timer stops the 
person last holding the item is disqualified from the game.
"""


def hot_potato(participants, num):
    """participants is a list of all the individual participating the game.
    While `num` counts the number the number of passing cycles in the game."""
    circle = Queue()  # Holds the names and position of the gamer participants
    for name in participants:
        circle.enqueue(name)

    while circle.size() > 1:
        for i in range(num):
            circle.enqueue(circle.dequeue())

        circle.dequeue()
    return circle.dequeue()


game = ["John", "Mary", "Luba", "Masha", "Mark", "Harry", "Ron"]
print(hot_potato(game, 9))
