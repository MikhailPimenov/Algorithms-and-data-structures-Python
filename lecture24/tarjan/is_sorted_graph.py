def is_sorted_graph(adjacency_lists: dict, numbers: dict) -> bool:
    if type(numbers) != dict:
        return False

    if len(adjacency_lists) == 0 or len(numbers) == 0:
        return False

    length = calculate_range(numbers)
    if length != len(numbers):
        return False

    if not is_continuous(numbers):
        return False

    return is_correct_order(adjacency_lists, numbers)


def is_correct_order(adjacency_lists: dict, numbers: dict) -> bool:
    for vertex in adjacency_lists:
        for neighbor in adjacency_lists[vertex]:
            if numbers[neighbor] <= numbers[vertex]:
                return False
    return True


def calculate_range(numbers: dict) -> int:
    maximum = max(*(numbers.values()))
    minimum = min(*(numbers.values()))

    return maximum - minimum + 1


def is_continuous(numbers: dict) -> int:
    present = [False] * (len(numbers) + 1)

    for vertex in numbers:
        if numbers[vertex] < len(present):
            present[numbers[vertex]] = True

    result = True
    one_false_allowed = True
    for k in range(len(present)):
        if one_false_allowed and not present[k]:
            one_false_allowed = False
            continue
        result = result and present[k]

    return result
