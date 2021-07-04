def count_connected_components5(G: dict) -> int:
    used = set()
    counter = 0

    for vertex in G:
        if vertex not in used:
            depth_first_search(vertex, G, used)
            counter += 1

    return counter


def depth_first_search(start, G: dict, used: set) -> None:
    used.add(start)

    for neighbor in G[start]:
        if neighbor not in used:
            depth_first_search(neighbor, G, used)
