"""Binary search algorithms are best suited for ordered list as the have
better search efficiency and improve the number of comparisons the algorithm
has to make to find a specified item"""


def binary_search(input_list, item):
    first_index = 0
    last_index = len(input_list) - 1
    found = False
    while first_index <= last_index and not found:
        mid_point = (first_index + last_index) // 2
        if input_list[mid_point] == item:
            found = True
        elif item < input_list[mid_point]:
            last_index = mid_point - 1
        else:
            first_index = mid_point + 1

    return found


mock_list = sorted([60, 30, 90, 120, 10, 20, 50])
print(binary_search(mock_list, 60))
