from collections import deque


def dijkstra(adjacency_lists: dict, start) -> dict:
    distances = get_distances(adjacency_lists, start)

    calculate_distances(adjacency_lists, start, distances)

    return distances


def get_distances(adjacency_lists: dict, start) -> dict:
    distances = {vertex: None for vertex in adjacency_lists}
    distances[start] = 0
    return distances


def calculate_distances(adjacency_lists, start, distances):
    queue = deque()
    queue.append(start)

    while queue:
        current_vertex = queue.popleft()
        for neighbor in adjacency_lists[current_vertex]:
            old_distance = distances[neighbor]
            new_distance = distances[current_vertex] + adjacency_lists[current_vertex][neighbor]
            if old_distance is None or new_distance < old_distance:
                distances[neighbor] = new_distance
                queue.append(neighbor)
