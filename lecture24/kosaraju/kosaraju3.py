def decorator_kosaraju3(wrappee):
    def wrapper(*args, **kwargs):
        result = wrappee(*args, **kwargs)
        return len(result)

    return wrapper


@decorator_kosaraju3
def kosaraju3(graph: dict) -> dict:
    used = set()
    stack = []

    for vertex in graph:
        if vertex not in used:
            depth_first_search_forward(graph, vertex, used, stack)

    reversed_graph = reverse_graph(graph)
    used.clear()
    components = []

    while stack:
        vertex = stack.pop()
        if vertex not in used:
            component = set()
            depth_first_search_backward(reversed_graph, vertex, used, component)
            components.append(component)

    return components


def depth_first_search_forward(graph: dict, vertex, used: set, stack: list):
    used.add(vertex)

    for neighbor in graph[vertex]:
        if neighbor not in used:
            depth_first_search_forward(graph, neighbor, used, stack)

    stack.append(vertex)


def depth_first_search_backward(graph: dict, vertex, used: set, component: set):
    used.add(vertex)
    component.add(vertex)

    for neighbor in graph[vertex]:
        if neighbor not in used:
            depth_first_search_backward(graph, neighbor, used, component)


def reverse_graph(graph: dict):
    reversed_graph = dict()

    for vertex in graph:
        if vertex not in reversed_graph:
            reversed_graph[vertex] = set()

    for vertex in graph:
        for neighbor in graph[vertex]:
            reversed_graph[neighbor].add(vertex)

    return reversed_graph
