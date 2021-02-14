from collections import deque


def dijkstra(graph: dict, start, finish="return_distances"):
    distances = calculate_distances(graph, start)

    if finish == "return_distances":
        return convert_distances(distances)

    path = reveal_path(graph, distances, start, finish)
    return path


def convert_distances(distances: dict):
    for v in distances:
        if distances[v] == float("+inf"):
            distances[v] = None
    return distances


def calculate_distances(graph: dict, start):
    queue = deque()
    queue.append(start)

    distances = {v: float("+inf") for v in graph}
    distances[start] = 0

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if distances[neighbor] > distances[current] + graph[current][neighbor]:
                distances[neighbor] = distances[current] + graph[current][neighbor]
                queue.append(neighbor)
    return distances


def reveal_path(graph: dict, distances: dict, start, finish):
    path = [finish]
    current = finish

    while current != start:
        for neighbor in graph[current]:
            if distances[neighbor] == distances[current] - graph[current][neighbor]:
                path.append(neighbor)
                current = neighbor
                break
    path.reverse()
    return path
