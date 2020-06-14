# lecture 25 part 2 and 3 of 3
# graphs
# width_first_search
# chess_horse_path

from collections import deque


def create_vertex(k: int, j: int):
    letters = "abcdefgh"
    numbers = "12345678"

    if 0 <= k < 8 and 0 <= j < 8:
        vertex = letters[k] + numbers[j]
        return vertex

    return "XX"


def add_vertex(adjacency_list: dict, k: int, j: int):
    vertex = create_vertex(k, j)
    adjacency_list[vertex] = set()


def add_vertexes(adjacency_list):
    for k in range(8):
        for j in range(8):
            add_vertex(adjacency_list, k, j)


def add_edge(adjacency_list: dict, vertex1, vertex2):
    adjacency_list[vertex1].add(vertex2)
    adjacency_list[vertex2].add(vertex1)


def add_edges(adjacency_list):
    for k in range(8):
        for j in range(8):
            vertex1 = create_vertex(k, j)
            if 0 <= k + 1 < 8 and 0 <= j + 2 < 8:
                vertex2 = create_vertex(k + 1, j + 2)
                add_edge(adjacency_list, vertex1, vertex2)
            if 0 <= k + 2 < 8 and 0 <= j + 1 < 8:
                vertex2 = create_vertex(k + 2, j + 1)
                add_edge(adjacency_list, vertex1, vertex2)
            if 0 <= k - 1 < 8 and 0 <= j + 2 < 8:
                vertex2 = create_vertex(k - 1, j + 2)
                add_edge(adjacency_list, vertex1, vertex2)
            if 0 <= k - 2 < 8 and 0 <= j + 1 < 8:
                vertex2 = create_vertex(k - 2, j + 1)
                add_edge(adjacency_list, vertex1, vertex2)
            if 0 <= k + 1 < 8 and 0 <= j - 2 < 8:
                vertex2 = create_vertex(k + 1, j - 2)
                add_edge(adjacency_list, vertex1, vertex2)
            if 0 <= k + 2 < 8 and 0 <= j - 1 < 8:
                vertex2 = create_vertex(k + 2, j - 1)
                add_edge(adjacency_list, vertex1, vertex2)
            if 0 <= k - 1 < 8 and 0 <= j - 2 < 8:
                vertex2 = create_vertex(k - 1, j - 2)
                add_edge(adjacency_list, vertex1, vertex2)
            if 0 <= k - 2 < 8 and 0 <= j - 1 < 8:
                vertex2 = create_vertex(k - 2, j - 1)
                add_edge(adjacency_list, vertex1, vertex2)


def create_graph():
    adjacency_list = dict()

    add_vertexes(adjacency_list)
    add_edges(adjacency_list)

    return adjacency_list


def chess_horse_graph(start_vertex, end_vertex):
    adjacency_list = create_graph()

    distance = dict()
    distance[start_vertex] = 0

    gray_and_black = set()
    gray_and_black.add(start_vertex)

    queue = deque()
    queue.append(start_vertex)

    stop_flag = False
    while len(queue) > 0 and not stop_flag:
        current_vertex = queue.popleft()

        for neighbour in adjacency_list[current_vertex]:
            if neighbour not in gray_and_black:
                gray_and_black.add(neighbour)
                queue.append(neighbour)
                distance[neighbour] = distance[current_vertex] + 1
                if neighbour == end_vertex:
                    stop_flag = True

    path = list()
    path.append(end_vertex)

    current_vertex = end_vertex
    for k in range(distance[end_vertex]):
        for neighbour in adjacency_list[current_vertex]:
            if neighbour in gray_and_black:
                if distance[neighbour] == distance[current_vertex] - 1:
                    path.append(neighbour)
                    current_vertex = neighbour
                    break

    path.reverse()
    return path


def test_chess_horse_graph(algorithm):
    start_vertex = "f7"
    end_vertex = "f6"
    path = algorithm(start_vertex, end_vertex)

    print("Path from", start_vertex, "to", end_vertex, ":")
    print(*path)

    start_vertex = "a1"
    end_vertex = "h8"
    path = algorithm(start_vertex, end_vertex)

    print("Path from", start_vertex, "to", end_vertex, ":")
    print(*path)


test_chess_horse_graph(chess_horse_graph)
