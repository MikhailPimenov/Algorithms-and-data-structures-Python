def kosaraju(graph: dict):
    stack = []
    gray_and_black = set()

    for v in graph:
        if v not in gray_and_black:
            depth_first_search_forward(graph, v, gray_and_black, stack)

    gray_and_black.clear()
    reversed_graph = reverse_graph(graph)
    components = []

    while stack:
        v = stack.pop()

        if v not in gray_and_black:
            components.append(set())
            for n in reversed_graph[v]:
                if n not in gray_and_black:
                    depth_first_search_backward(reversed_graph, n, gray_and_black, components[-1])

    return len(components)


def reverse_graph(graph: dict):
    reversed_graph = {}
    for v in graph:
        reversed_graph[v] = set()
    for v in graph:
        for n in graph[v]:
            reversed_graph[n].add(v)

    return reversed_graph


def depth_first_search_forward(graph: dict, start, gray_and_black: set, stack: list):
    gray_and_black.add(start)

    for n in graph[start]:
        if n not in gray_and_black:
            depth_first_search_forward(graph, n, gray_and_black, stack)
    stack.append(start)


def depth_first_search_backward(graph: dict, start, gray_and_black: set, component: set):
    gray_and_black.add(start)
    component.add(start)

    for n in graph[start]:
        if n not in gray_and_black:
            depth_first_search_backward(graph, n, gray_and_black, component)
