def tarjan3(graph: dict) -> dict:
    used = set()
    loop_detector = set()
    stack = []
    for vertex in graph:
        if vertex not in used:
            no_loop = depth_first_search(graph, vertex, used, stack, loop_detector)
            if not no_loop:
                return False

    number = 0
    numbers = dict()
    while stack:
        numbers[stack.pop()] = number
        number += 1

    return numbers


def depth_first_search(graph: dict, vertex, used: set, stack: list, loop_detector: set) -> bool:
    used.add(vertex)
    loop_detector.add(vertex)

    for neighbor in graph[vertex]:
        if neighbor in loop_detector:
            return False
        if neighbor not in used:
            no_loop = depth_first_search(graph, neighbor, used, stack, loop_detector)
            if not no_loop:
                return False

    stack.append(vertex)
    loop_detector.remove(vertex)
    return True
