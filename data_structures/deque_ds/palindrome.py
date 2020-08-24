from data_structures.deque_ds.deque import Deque


def palindrome(word):
    """Takes in a string and validates if it is a palindrome."""
    char_deque = Deque()

    for char in word.lower():
        char_deque.addRear(char)

    string_equal = True

    while char_deque.size() > 1 and string_equal:
        first = char_deque.removeFront()
        last = char_deque.removeRear()
        if first != last:
            string_equal = False

    return string_equal


print(palindrome(""))
