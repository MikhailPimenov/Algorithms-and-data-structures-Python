def reverse_graph(adjacency_lists: dict) -> dict:
    reversed_graph = {}

    for vertex in adjacency_lists:
        reversed_graph[vertex] = set()

    for vertex in reversed_graph:
        for neighbor in adjacency_lists[vertex]:
            reversed_graph[neighbor].add(vertex)

    return reversed_graph
