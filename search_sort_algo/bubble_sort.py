def bubble_sort(a_list):
    """Implementation for a complete bubble sort algorithm."""
    for num_pass in range(len(a_list) - 1, 0, -1):
        # num_pass represents the number of times the algorithm has traversed
        # through the list
        for i in range(num_pass):
            if a_list[i] > a_list[i + 1]:
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]


def short_bubble_sort(a_list):
    """Short bubble sort is a modification to the regular bubble sort
    algorithm. It stops traversing after several passes and it notices that a
    list is ordered """
    exchanges = True
    num_pass = len(a_list) - 1
    while num_pass > 0 and exchanges:
        exchanges = False
        for i in range(num_pass):
            if a_list[i] > a_list[i + 1]:
                exchanges = True
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
        num_pass -= 1


mock_list = [39, 23, 1, 9, 0, 88, 45, 60, 80, 100, 1001, 343, 959, 3524]
bubble_sort(mock_list)
print(mock_list)
