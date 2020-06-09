# lecture 23
# graphs
# create_adjacency_matrix
# create_adjacency_list
# create_compact_adjacency_list


def create_adjacency_matrix():
    print("Enter n, m:")
    n, m = input().split()

    n = int(n)
    m = int(m)

    vertex = []
    index = {}
    adjacency = [[0] * n for k in range(n)]

    for k in range(m):
        print("Enter edge:")
        v1, v2 = input().split()
        for v in v1, v2:
            if v not in vertex:
                vertex.append(v)
                index[v] = len(vertex) - 1
        adjacency[index[v1]][index[v2]] += 1
        adjacency[index[v2]][index[v1]] += 1

    result = [vertex, index, adjacency]
    return result


def create_adjacency_list():
    print("Enter n, m:")
    n, m = input().split()

    n = int(n)
    m = int(m)

    adjacency = {}

    for k in range(m):
        print("Enter edge:")
        v1, v2 = input().split()
        for x, y in (v1, v2), (v2, v1):
            if x not in adjacency:
                adjacency[x] = set()
                adjacency[x].add(y)
            else:
                adjacency[x].add(y)
    return adjacency


def create_compact_adjacency_list():
    adjacency = {'A': {'B', 'D'},
                 'B': {'A', 'C', 'D'},
                 'C': {'B', 'D'},
                 'D': {'A', 'B', 'C'}}

    index = {'A': 0, 'B': 1, 'C': 2, 'D': 3}

    compact_adjacency = []
    offset = [0]

    for v in adjacency:
        for neighbour in adjacency[v]:
            compact_adjacency.append(index[neighbour])
        offset.append(offset[len(offset) - 1] + len(adjacency[v]))

    result = [compact_adjacency, offset]

    return result


def test_adjacency_matrix(algorithm):
    """
    Enter n, m:
    4 5
    Enter edge:
    A B
    Enter edge:
    B C
    Enter edge:
    C D
    Enter edge:
    B D
    Enter edge:
    A D
    """

    result = algorithm()

    v2 = ['A', 'B', 'C', 'D']
    index2 = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    a2 = [[0, 1, 0, 1],
          [1, 0, 1, 1],
          [0, 1, 0, 1],
          [1, 1, 1, 0]]

    print("test #1:", "ok" if result == [v2, index2, a2] else "FAILED")


def test_adjacency_list(algorithm):
    """
    Enter n, m:
    4 5
    Enter edge:
    A B
    Enter edge:
    B C
    Enter edge:
    C D
    Enter edge:
    B D
    Enter edge:
    A D
    """

    result = algorithm()

    adjacency = {'A': {'B', 'D'},
                 'B': {'A', 'C', 'D'},
                 'C': {'B', 'D'},
                 'D': {'A', 'B', 'C'}}

    print("test #1:", "ok" if result == adjacency else "FAILED")


def test_compact_adjacency_list(algorithm):
    result = algorithm()
    adjacency = [1, 3, 2, 0, 3, 1, 3, 2, 1, 0]
    offset = [0, 2, 5, 7, 10]

    b_is_correct = True

    for k in range(len(offset) - 1):
        neighbour_list = adjacency[offset[k]:offset[k + 1]]
        for index in range(offset[k], offset[k + 1]):
            if result[0][index] not in neighbour_list:
                b_is_correct = False

    if result[1] != offset:
        b_is_correct = False

    print("test #1:", "ok" if b_is_correct else "FAILED")


test_adjacency_matrix(create_adjacency_matrix)
test_adjacency_list(create_adjacency_list)
test_compact_adjacency_list(create_compact_adjacency_list)
