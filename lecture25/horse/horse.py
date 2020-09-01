from collections import deque


def horse(start_vertex, finish_vertex) -> list:
    adjacency_lists = create_graph()
    distances = find_distances(adjacency_lists, start_vertex, finish_vertex)

    path = reveal_path(adjacency_lists, start_vertex, finish_vertex, distances)

    return path


def create_graph() -> dict:
    adjacency_lists = {}
    for i in range(8):
        for j in range(8):
            vertex = create_vertex(i, j)
            adjacency_lists[vertex] = set()

    for i in range(8):
        for j in range(8):
            vertex_1 = create_vertex(i, j)

            if 0 <= i + 2 < 8 and 0 <= j + 1 < 8:
                vertex_2 = create_vertex(i + 2, j + 1)
                add_edge(adjacency_lists, vertex_1, vertex_2)
            if 0 <= i + 1 < 8 and 0 <= j + 2 < 8:
                vertex_2 = create_vertex(i + 1, j + 2)
                add_edge(adjacency_lists, vertex_1, vertex_2)
            if 0 <= i + 2 < 8 and 0 <= j - 1 < 8:
                vertex_2 = create_vertex(i + 2, j - 1)
                add_edge(adjacency_lists, vertex_1, vertex_2)
            if 0 <= i + 1 < 8 and 0 <= j - 2 < 8:
                vertex_2 = create_vertex(i + 1, j - 2)
                add_edge(adjacency_lists, vertex_1, vertex_2)
            if 0 <= i - 2 < 8 and 0 <= j + 1 < 8:
                vertex_2 = create_vertex(i - 2, j + 1)
                add_edge(adjacency_lists, vertex_1, vertex_2)
            if 0 <= i - 1 < 8 and 0 <= j + 2 < 8:
                vertex_2 = create_vertex(i - 1, j + 2)
                add_edge(adjacency_lists, vertex_1, vertex_2)
            if 0 <= i - 2 < 8 and 0 <= j - 1 < 8:
                vertex_2 = create_vertex(i - 2, j - 1)
                add_edge(adjacency_lists, vertex_1, vertex_2)
            if 0 <= i - 1 < 8 and 0 <= j - 2 < 8:
                vertex_2 = create_vertex(i - 1, j - 2)
                add_edge(adjacency_lists, vertex_1, vertex_2)
    return adjacency_lists


def create_vertex(i: int, j: int) -> str:
    letters = "abcdefgh"
    numbers = "12345678"

    assert i >= 0
    assert j >= 0
    assert i < 8
    assert j < 8

    return letters[i] + numbers[j]


def add_edge(adjacency_lists: dict, vertex_1, vertex_2):
    adjacency_lists[vertex_1].add(vertex_2)
    adjacency_lists[vertex_2].add(vertex_1)


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


def reveal_path(adjacency_lists: dict, start_vertex, finish_vertex, distances: dict) -> list:
    reversed_path = [finish_vertex]

    current_vertex = finish_vertex

    while current_vertex != start_vertex:
        for neighbor in adjacency_lists[current_vertex]:
            if distances[neighbor] == distances[current_vertex] - 1:
                reversed_path.append(neighbor)
                current_vertex = neighbor
                break

    return reversed_path[::-1]
