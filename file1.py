# lecture 25 part 1 of 3
# graphs
# width_first_search
# distances

from collections import deque


def distances(vertex, adjacency_list: dict):
    gray_and_black = set()

    distance = {k: 0 for k in adjacency_list}
    gray_and_black.add(vertex)
    distance[vertex] = 0
    queue = deque(vertex)

    while len(queue):
        current_vertex = queue.popleft()
        for neighbour in adjacency_list[current_vertex]:
            if neighbour not in gray_and_black:
                gray_and_black.add(neighbour)
                queue.append(neighbour)
                distance[neighbour] = distance[current_vertex] + 1

    return distance


def test_distances(algorithm):
    print("testing distances:")

    adjacency_list = {'A': {'B', 'C', 'D', 'E'},
                      'B': {'A', 'C', 'F', 'G'},
                      'C': {'A', 'C', 'D', 'J'},
                      'D': {'A', 'L', 'K'},
                      'E': {'M', 'N'},
                      'F': {'B'},
                      'G': {'B', 'H', 'I'},
                      'H': {'G'},
                      'I': {'G'},
                      'J': {'C'},
                      'K': {'O', 'P', 'D'},
                      'L': {'R', 'S', 'D'},
                      'M': {'T', 'E'},
                      'N': {'E'},
                      'O': {'K'},
                      'P': {'K'},
                      'R': {'L'},
                      'S': {'L'},
                      'T': {'M'}, }

    distances1 = {'A': 0,
                  'B': 1,
                  'C': 1,
                  'D': 1,
                  'E': 1,
                  'F': 2,
                  'G': 2,
                  'H': 3,
                  'I': 3,
                  'J': 2,
                  'K': 2,
                  'L': 2,
                  'M': 2,
                  'N': 2,
                  'O': 3,
                  'P': 3,
                  'R': 3,
                  'S': 3,
                  'T': 3, }

    distances2 = algorithm('A', adjacency_list)

    print("test #1:", "ok" if distances1 == distances2 else "FAILED")

    distances1 = {'A': 3,
                  'B': 4,
                  'C': 4,
                  'D': 2,
                  'E': 4,
                  'F': 5,
                  'G': 5,
                  'H': 6,
                  'I': 6,
                  'J': 5,
                  'K': 1,
                  'L': 3,
                  'M': 5,
                  'N': 5,
                  'O': 0,
                  'P': 2,
                  'R': 4,
                  'S': 4,
                  'T': 6, }

    distances2 = algorithm('O', adjacency_list)
    print("test #2:", "ok" if distances1 == distances2 else "FAILED")


test_distances(distances)
