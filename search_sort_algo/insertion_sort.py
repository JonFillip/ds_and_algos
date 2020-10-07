def insertion_sort(a_list):
    """Insertion sort implementation."""
    for index in range(1, len(a_list)):

        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position -= 1

        a_list[position] = current_value


mock_list = [39, 23, 1, 9, 0, 88, 45, 60, 80, 100, 1001, 343, 959, 3524]
insertion_sort(mock_list)
print(mock_list)
