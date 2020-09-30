# Algorithms for sequential search for unordered and ordered list

def sequential_search(input_list, item):
    """Sequential search algorithm for an unordered list."""
    index = 0
    found = False
    while index < len(input_list) and not found:
        if input_list[index] == item:
            found = True
        else:
            index += 1
    return found


def ordered_sequential_search(input_list, item):
    """Sequential search algorithm for an ordered list."""
    index = 0
    found = False
    stop = False
    while index < len(input_list) and not found and not stop:
        if input_list[index] == item:
            found = True
        elif input_list[index] > item:
            stop = True
        else:
            index += 1

    return found


list_1 = [1, 4, 5, 6, 84, 100, 12, 77, 3, 23, 33]
list_2 = sorted(list_1)
print(sequential_search(list_1, 3))
print(ordered_sequential_search(list_2, 99))
