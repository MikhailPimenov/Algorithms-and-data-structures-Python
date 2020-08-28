from typing import List


def adjacency_matrix():
    m, n = input().split()
    m = int(m)
    n = int(n)

    V = []
    index = dict()
    matrix = [([0] * (m + 1)) for k in range(m + 1)]

    v_index = 1
    for k in range(n):
        v1, v2 = input().split()

        for v in v1, v2:
            if v not in V:
                V.append(v)
            if v not in index:
                index[v] = v_index
                v_index += 1
        v1_index = index[v1]
        v2_index = index[v2]
        matrix[v1_index][v2_index] += 1
        matrix[v2_index][v1_index] += 1
    return V, index, matrix
