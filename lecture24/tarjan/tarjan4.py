class LoopDetectionError(ValueError):
    def __init__(self, info="Loop detected"):
        self.info = info


def tarjan4(g: dict) -> dict:
    used = set()
    loop_detector = set()
    stack = []

    try:
        for vertex in g:
            if vertex not in used:
                depth_first_search(g, vertex, used, loop_detector, stack)
    except LoopDetectionError:
        return {}

    n = dict()
    number = 0
    while stack:
        n[stack.pop()] = number
        number += 1

    return n


def depth_first_search(g: dict, start, used: set, loop_detector: set, stack: list):
    used.add(start)
    loop_detector.add(start)

    for neighbor in g[start]:
        if neighbor in loop_detector:
            raise LoopDetectionError
        if neighbor not in used:
            depth_first_search(g, neighbor, used, loop_detector, stack)

    stack.append(start)
    loop_detector.remove(start)
