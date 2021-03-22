def count_connected_components3(graph:dict):
    counter = 0
    used = set()

    for vertex in graph:
        if vertex not in used:
            counter += 1
            depth_first_search(graph, vertex, used)

    return counter


def depth_first_search(graph:dict, start, used:set):
    used.add(start)

    for neighbour in graph[start]:
        if neighbour not in used:
            depth_first_search(graph, neighbour, used)