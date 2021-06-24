def floyd_uolsher4(g: dict) -> dict:
    v = [None] * (len(g) + 1)
    i = 1
    for vertex in g:
        v[i] = vertex
        i += 1

    f = [{vertex1: {vertex2: 0 for vertex2 in g} for vertex1 in g} for _ in range(2)]

    for vertex1 in g:
        for vertex2 in g:
            if vertex2 in g[vertex1]:
                f[0][vertex1][vertex2] = g[vertex1][vertex2]
            else:
                f[0][vertex1][vertex2] = float('+inf')

    for vertex in g:
        f[0][vertex][vertex] = 0

    for k in range(1, len(g) + 1):
        for i in range(1, len(g) + 1):
            for j in range(1, len(g) + 1):
                f[k % 2][v[i]][v[j]] = min(f[(k - 1) % 2][v[i]][v[j]],
                                           f[(k - 1) % 2][v[i]][v[k]] + f[(k - 1) % 2][v[k]][v[j]])

    return f[len(g) % 2]
