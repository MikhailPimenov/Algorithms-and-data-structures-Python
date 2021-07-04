class LoopError(Exception):
    pass


def tarjan5(G: dict) -> dict:
    used = set()
    stack = list()
    loop_detector = set()

    try:
        for vertex in G:
            if vertex not in used:
                depth_first_search(vertex, G, used, stack, loop_detector)
    except LoopError:
        return {}

    number = 0
    numbers = {}

    while stack:
        vertex = stack.pop()
        numbers[vertex] = number
        number += 1

    return numbers


def depth_first_search(start, G: dict, used: set, stack: list, loop_detector: set):
    used.add(start)
    loop_detector.add(start)

    for neighbor in G[start]:
        if neighbor in loop_detector:
            raise LoopError
        if neighbor not in used:
            depth_first_search(neighbor, G, used, stack, loop_detector)

    stack.append(start)
    loop_detector.remove(start)
