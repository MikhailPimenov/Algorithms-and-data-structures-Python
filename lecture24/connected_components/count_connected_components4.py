def count_connected_components4(g: dict) -> int:
    used = set()
    counter = 0

    for vertex in g:
        if vertex not in used:
            counter += 1
            depth_first_search(g, vertex, used)

    return counter


def depth_first_search(g: dict, start, used: set):
    used.add(start)

    for neighbor in g[start]:
        if neighbor not in used:
            depth_first_search(g, neighbor, used)
