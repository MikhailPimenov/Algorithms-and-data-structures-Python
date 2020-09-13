import math


def floyd_uolsher(adjacency_lists: dict) -> dict:
    f0 = set_initial_distances(adjacency_lists)

    f = [f0] * (len(adjacency_lists)+1)
    v = [key for key in adjacency_lists.keys()]
    for k in range(1, len(v)+1):
        for i in range(len(v)):
            for j in range(len(v)):
                if i != j:
                    f[k][v[i]][v[j]] = min(f[k - 1][v[i]][v[j]],
                                           f[k - 1][v[i]][v[k-1]] + f[k - 1][v[k-1]][v[j]])
                else:
                    f[k][v[i]][v[j]] = 0

    return f[-1]


def set_initial_distances(adjacency_lists: dict) -> dict:
    distances = {v_i: {} for v_i in adjacency_lists}
    for v_i in adjacency_lists:
        for v_j in adjacency_lists:
            if v_i not in adjacency_lists[v_j] and v_j not in adjacency_lists[v_i]:
                distances[v_i][v_j] = math.inf
                distances[v_j][v_i] = math.inf
            else:
                if v_i in adjacency_lists[v_j]:
                    distances[v_j][v_i] = adjacency_lists[v_j][v_i]
                if v_j in adjacency_lists[v_i]:
                    distances[v_i][v_j] = adjacency_lists[v_i][v_j]
    return distances
