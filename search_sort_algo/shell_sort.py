"""The following shell sort algorithm uses Shell's increment gap."""


def shell_sort(a_list):
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_pos in range(sublist_count):
            gap_insertion_sort(a_list, start_pos, sublist_count)

        print(f"After increment of size {sublist_count}, The list is {a_list}")

        sublist_count //= 2


def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
        a_list[position] = current_value


mock_list = [39, 23, 1, 9, 0, 88, 45, 60, 80, 100, 1001, 343, 959, 3524]
shell_sort(mock_list)
print(mock_list)
