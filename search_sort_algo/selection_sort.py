def selection_sort(a_list):
    """Implementation for selection sort."""
    for slot in range(len(a_list) - 1, 0, -1):
        max_value_pos = 0
        for location in range(1, slot + 1):
            if a_list[location] > a_list[max_value_pos]:
                max_value_pos = location

        a_list[slot], a_list[max_value_pos] = a_list[max_value_pos], a_list[
            slot]


mock_list = [39, 23, 1, 9, 0, 88, 45, 60, 80, 100, 1001, 343, 959, 3524]
selection_sort(mock_list)
print(mock_list)
