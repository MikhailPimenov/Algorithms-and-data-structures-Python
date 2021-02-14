def connected_components(graph: dict):
    gray_and_black = set()
    counter = 0
    for v in graph:
        if v not in gray_and_black:
            depth_first_search(graph, v, gray_and_black)
            counter += 1
    return counter


def depth_first_search(graph: dict, start, gray_and_black: set):
    gray_and_black.add(start)

    for neighbor in graph[start]:
        if neighbor not in gray_and_black:
            depth_first_search(graph, neighbor, gray_and_black)
