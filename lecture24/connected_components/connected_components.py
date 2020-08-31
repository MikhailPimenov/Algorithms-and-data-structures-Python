def connected_components(adjacency_lists: dict) -> int:
    gray_and_black = set()

    result = 0
    for vertex in adjacency_lists:
        if vertex not in gray_and_black:
            depth_first_search(adjacency_lists, vertex, gray_and_black)
            result += 1
    return result


def depth_first_search(adjacency_lists: dict, start_vertex, gray_and_black: set):
    gray_and_black.add(start_vertex)

    for neighbor in adjacency_lists[start_vertex]:
        if neighbor not in gray_and_black:
            depth_first_search(adjacency_lists, neighbor, gray_and_black)
