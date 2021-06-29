def floyd_uolsher5(G: dict) -> dict:
    v = [None] * (len(G) + 1)

    i = 1
    for vertex in G:
        v[i] = vertex
        i += 1

    F0 = {
        vertex1:
            {
                vertex2: G[vertex1][vertex2]
                if vertex2 in G[vertex1] else float("+inf")
                for vertex2 in G
            }
        for vertex1 in G
    }

    for vertex in G:
        F0[vertex][vertex] = 0

    F = [F0, F0]

    for k in range(1, len(G) + 1):
        for i in range(1, len(G) + 1):
            for j in range(1, len(G) + 1):
                F[k % 2][v[i]][v[j]] = min(F[(k - 1) % 2][v[i]][v[j]],
                                           F[(k - 1) % 2][v[i]][v[k]] + F[(k - 1) % 2][v[k]][v[j]])

    return F[len(G) % 2]
