# Lecture 6
# insertion_sort
# selection_sort
# bubble_sort

def insertion_sort(list):
    """
    Sorts list inserting next element in sorted part of list
    :param list: list to be sorted
    :return:
    """
    N = len(list)

    for top in range(1, N):
        k = top
        while k > 0 and list[k - 1] > list[k]:
            list[k], list[k - 1] = list[k - 1], list[k]
            k -= 1


def selection_sort(list):
    """
    Sorts list selecting next element in not sorted part and adding it to sorted part
    :param list: list to be sorted
    :return:
    """
    N = len(list)

    for pos in range(N - 1):
        element = list[pos]
        index = pos
        for k in range(pos + 1, N):
            if list[k] < element:
                element = list[k]
                index = k
        list[index], list[pos] = list[pos], list[index]


def bubble_sort(list):
    """
    Sorts list moving 'lightest' element to the end of list.
    :param list: list to be sorted
    :return:
    """
    N = len(list)

    for k in range(N - 1):
        for j in range(N - 1 - k):
            if list[j + 1] < list[j]:
                list[j + 1], list[j] = list[j], list[j + 1]


def test_sort(sorting_algorithm):
    print("Testing: ", sorting_algorithm.__doc__)

    list = [1, 3, 2, 5, 4]
    list_sorted = [1, 2, 3, 4, 5]

    print("Test #1: ", end="")
    sorting_algorithm(list)
    print("ok" if list == list_sorted else "FAILED")

    list = [2, 2, 1, 0, 5]
    list_sorted = [0, 1, 2, 2, 5]

    print("Test #2: ", end="")
    sorting_algorithm(list)
    print("ok" if list == list_sorted else "FAILED")

    list = [1, 3, 2, 5, 4, 1, 1, 2, 7, 5, 6, 6, 3]
    list_sorted = [1, 1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7]

    print("Test #3: ", end="")
    sorting_algorithm(list)
    print("ok" if list == list_sorted else "FAILED")


test_sort(insertion_sort)
test_sort(selection_sort)
test_sort(bubble_sort)
