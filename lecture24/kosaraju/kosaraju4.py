def kosaraju4(g: dict) -> int:
    used = set()
    stack = []
    for vertex in g:
        if vertex not in used:
            depth_first_search_forward(g, vertex, used, stack)

    rg = reverse_graph(g)
    used.clear()
    components = []
    while stack:
        vertex = stack.pop()
        if vertex not in used:
            component = set()
            depth_first_search_backward(rg, vertex, used, component)
            components.append(component)

    return len(components)


def depth_first_search_forward(g: dict, start, used: set, stack: list):
    used.add(start)

    for neighbor in g[start]:
        if neighbor not in used:
            depth_first_search_forward(g, neighbor, used, stack)

    stack.append(start)


def depth_first_search_backward(g: dict, start, used: set, component: set):
    used.add(start)
    component.add(start)

    for neighbor in g[start]:
        if neighbor not in used:
            depth_first_search_backward(g, neighbor, used, component)


def reverse_graph(g: dict) -> dict:
    rg = dict()
    for vertex in g:
        rg[vertex] = set()

    for vertex in g:
        for neighbor in g[vertex]:
            rg[neighbor].add(vertex)

    return rg
