def merge_sort(a_list):
    """Implementation of a merge sort using recursion."""
    if len(a_list) <= 1:
        print(a_list)

    elif len(a_list) > 1:
        print(f"Splitting: {a_list}")
        mid_point = len(a_list) // 2
        left_half = a_list[:mid_point]
        right_half = a_list[mid_point:]

        merge_sort(left_half)
        merge_sort(right_half)

        first = 0  # Represents the 1st item in the split list of 2 items
        second = 0  # Represents the 2nd item in the split list of 2 items
        third = 0  # Represents the 3rd item in the split list contain an odd
        # number of item e.g a split list with three items

        while first < len(left_half) and second < len(right_half):
            if left_half[first] < right_half[second]:
                a_list[third] = left_half[first]
                first += 1
            else:
                a_list[third] = right_half[second]
                second += 1
            third += 1

        while first < len(left_half):
            a_list[third] = left_half[first]
            first += 1
            third += 1

        while second < len(right_half):
            a_list[third] = right_half[second]
            second += 1
            third += 1
    print(f"Merging {a_list}")


mock_list = [39, 23, 1, 9, 0, 88, 45, 60, 80, 100, 1001, 343, 959, 3520]
merge_sort(mock_list)
