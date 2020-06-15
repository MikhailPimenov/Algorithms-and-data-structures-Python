# lecture 28
# graphs
# floyd_uolsher



def calculate_max(adjacency_list: dict):
    result = 0

    for k in adjacency_list:
        for i in adjacency_list[k]:
            result += adjacency_list[k][i]

    return result * 10


def create_indexes(adjacency_list: dict):
    indexes = dict()

    index = 0
    for k in adjacency_list:
        indexes[k] = index
        index += 1

    return indexes


def create_distances(adjacency_list: dict, index: dict):
    unreachable_max = calculate_max(adjacency_list)

    distances = [[unreachable_max] * len(adjacency_list) for k in range(len(adjacency_list))]

    for j in adjacency_list:
        distances[index[j]][index[j]] = 0
        for i in adjacency_list[j]:
            distances[index[j]][index[i]] = adjacency_list[j][i]

    return distances


def floyd_uolsher(adjacency_list: dict):
    index = create_indexes(adjacency_list)
    distances = create_distances(adjacency_list, index)

    temp = distances[:]

    for k in adjacency_list:
        for i in adjacency_list:
            for j in adjacency_list:
                distances[index[i]][index[j]] = min(temp[index[i]][index[j]],
                                                    temp[index[i]][index[k]] + temp[index[k]][index[j]])
        temp = distances[:]

    return distances


def test_floyd_uolsher(algorithm):
    print("testing: floyd_uolsher")
    adjacency_list = {
        'A': {'B': 2,
              'H': 15},
        'B': {'C': 1,
              'D': 5,
              'A': 2},
        'C': {'B': 1,
              'D': 3,
              'F': 2,
              'G': 1},
        'D': {'B': 5,
              'C': 3,
              'F': 4,
              'E': 6},
        'E': {'D': 6,
              'F': 7,
              'I': 2},
        'F': {'G': 1,
              'C': 2,
              'D': 4,
              'E': 7,
              'H': 3},
        'G': {'C': 1,
              'F': 1},
        'H': {'F': 3,
              'I': 12,
              'A': 15},
        'I': {'E': 2,
              'H': 12}
    }

    distances = floyd_uolsher(adjacency_list)
    for k in distances:
        print(*k)


test_floyd_uolsher(calculate_max)
