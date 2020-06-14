# lecture 26
# graphs
# width_first_search
# dijkstra

from collections import deque


def dijkstra(start, end, adjacency_list: dict) -> list:
    queue = deque()
    queue.append(start)

    distances = {k: float("inf") for k in adjacency_list}
    distances[start] = 0

    while queue:
        current_vertex = queue.popleft()
        for neighbour in adjacency_list[current_vertex]:
            if distances[neighbour] > distances[current_vertex] + adjacency_list[current_vertex][neighbour]:
                distances[neighbour] = distances[current_vertex] + adjacency_list[current_vertex][neighbour]
                queue.append(neighbour)

    path = [end]
    current_vertex = end
    while current_vertex != start:
        for neighbour in adjacency_list[current_vertex]:
            if distances[neighbour] == distances[current_vertex] - adjacency_list[current_vertex][neighbour]:
                path.append(neighbour)
                current_vertex = neighbour
                break

    path.reverse()
    return [distances[end], path]


def test_dijkstra(algorithm):
    print("testing: dijkstra")
    adjacency_list = {
        'A': {'B': 2, 'H': 15},
        'B': {'C': 1, 'D': 5, 'A': 2},
        'C': {'B': 1, 'D': 3, 'F': 2, 'G': 1},
        'D': {'B': 5, 'C': 3, 'F': 4, 'E': 6},
        'E': {'D': 6, 'F': 7, 'I': 2},
        'F': {'G': 1, 'C': 2, 'D': 4, 'E': 7, 'H': 3},
        'G': {'C': 1, 'F': 1},
        'H': {'F': 3, 'I': 12, 'A': 15},
        'I': {'E': 2, 'H': 12}
    }

    start = 'A'
    end = 'I'

    result = algorithm(start, end, adjacency_list)

    print("Path from", start, "to", end, "costs", result[0], ":")
    print(*(result[1]))


test_dijkstra(dijkstra)
