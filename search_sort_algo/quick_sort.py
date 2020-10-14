def quick_sort(an_array):
    quick_sort_helper(an_array, 0, len(an_array) - 1)


def quick_sort_helper(an_array, start, end):
    if start < end:
        split_point = partition(an_array, start, end)

        quick_sort_helper(an_array, start, split_point - 1)
        quick_sort_helper(an_array, split_point + 1, end)


def partition(an_array, start, end):
    """Implementation using the Hoare Partition Scheme."""
    pivot = an_array[start]

    left_mark = start + 1
    right_mark = end

    done = False
    while not done:

        while left_mark <= right_mark and an_array[left_mark] <= pivot:
            left_mark += 1

        while right_mark >= left_mark and an_array[left_mark] >= pivot:
            right_mark -= 1

        if right_mark < left_mark:
            done = True
        else:
            an_array[left_mark], an_array[right_mark] = an_array[right_mark], \
                                                        an_array[left_mark]

    an_array[start], an_array[right_mark] = an_array[right_mark], an_array[start]

    return right_mark


mock_list = [48, 5, 10, 8, 11, 21, 34, 58, 60, 100]
quick_sort(mock_list)
print(mock_list)