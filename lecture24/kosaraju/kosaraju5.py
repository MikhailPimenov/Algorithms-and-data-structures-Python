def kosaraju5(G: dict) -> set:
    stack = []
    used = set()
    for vertex in G:
        if vertex not in used:
            depth_first_search_forward(vertex, G, used, stack)

    used.clear()
    components = set()
    Gr = reverse_graph(G)

    while stack:
        vertex = stack.pop()
        if vertex not in used:
            component = set()
            depth_first_search_backward(vertex, Gr, used, component)
            components.add(frozenset(component))

    return components


def depth_first_search_forward(start, G: dict, used: set, stack: list):
    used.add(start)
    for neighbor in G[start]:
        if neighbor not in used:
            depth_first_search_forward(neighbor, G, used, stack)
    stack.append(start)


def depth_first_search_backward(start, Gr: dict, used: set, component: set):
    used.add(start)
    component.add(start)

    for neighbor in Gr[start]:
        if neighbor not in used:
            depth_first_search_backward(neighbor, Gr, used, component)


def reverse_graph(G: dict) -> dict:
    Gr = {vertex: set() for vertex in G}

    for vertex in G:
        for neighbor in G[vertex]:
            Gr[neighbor].add(vertex)

    return Gr
