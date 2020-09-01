from collections import deque


def path(adjacency_lists: dict, start_vertex, finish_vertex) -> list:
    distances = find_distances(adjacency_lists, start_vertex, finish_vertex)
    path = reveal_path(adjacency_lists, start_vertex, finish_vertex, distances)

    return path


def find_distances(adjacency_lists: dict, start_vertex, finish_vertex) -> dict:
    distances = {vertex: None for vertex in adjacency_lists}
    distances[start_vertex] = 0
    queue = deque()

    queue.append(start_vertex)

    while len(queue) > 0:
        current_vertex = queue.popleft()

        for neighbor in adjacency_lists[current_vertex]:
            if distances[neighbor] is None:
                distances[neighbor] = distances[current_vertex] + 1
                if neighbor == finish_vertex:
                    break
                queue.append(neighbor)
    return distances


def reveal_path(adjacency_lists, start_vertex, finish_vertex, distances):
    current_vertex = finish_vertex
    reversed_path = [current_vertex]

    while current_vertex != start_vertex:
        for neighbor in adjacency_lists[current_vertex]:
            if distances[neighbor] == distances[current_vertex] - 1:
                reversed_path.append(neighbor)
                current_vertex = neighbor
                break
    return reversed_path[::-1]
