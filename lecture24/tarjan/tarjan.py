def tarjan(adjacency_lists: dict) -> dict:
    numbers = {}

    gray_and_black = set()
    gray = set()
    stack = []
    for vertex in adjacency_lists:
        if vertex not in gray:
            if vertex not in gray_and_black:
                no_cycles = depth_first_search(adjacency_lists, vertex, gray_and_black, stack, gray)
                if not no_cycles:
                    return {}
                stack.append(vertex)
        else:
            return {}

    number = 0
    while len(stack):
        current_vertex = stack.pop()
        numbers[current_vertex] = number
        number += 1

    return numbers


def depth_first_search(adjacency_lists: dict, start_vertex, gray_and_black: set, stack: list, gray: set()) -> bool:
    gray_and_black.add(start_vertex)
    gray.add(start_vertex)

    for neighbor in adjacency_lists[start_vertex]:
        if neighbor not in gray:
            if neighbor not in gray_and_black:
                no_cycles = depth_first_search(adjacency_lists, neighbor, gray_and_black, stack, gray)
                if not no_cycles:
                    return False
                stack.append(neighbor)
                gray.remove(neighbor)
        else:
            return False
    return True
