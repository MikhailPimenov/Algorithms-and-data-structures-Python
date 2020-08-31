from .reverse_graph import reverse_graph


def kosaraju(adjacency_lists: dict) -> int:
    gray_and_black = set()
    stack = []

    for vertex in adjacency_lists:
        if vertex not in gray_and_black:
            depth_first_search(adjacency_lists, vertex, gray_and_black, set(), stack, True)
            stack.append(vertex)

    gray_and_black.clear()
    components = {}
    result = 0

    adjacency_lists = reverse_graph(adjacency_lists)
    while len(stack):
        start_vertex = stack.pop()
        if start_vertex not in gray_and_black:
            component = set()
            depth_first_search(adjacency_lists, start_vertex, gray_and_black, component, stack, False)
            components[result] = component
            result += 1
    return result


def depth_first_search(adjacency_lists: dict, start_vertex, gray_and_black: set, component: set, stack: list,
                       forward: bool = True):
    gray_and_black.add(start_vertex)
    if not forward:
        component.add(start_vertex)

    for neighbor in adjacency_lists[start_vertex]:
        if neighbor not in gray_and_black:
            depth_first_search(adjacency_lists, neighbor, gray_and_black, component, stack, forward)
            if forward:
                stack.append(neighbor)
