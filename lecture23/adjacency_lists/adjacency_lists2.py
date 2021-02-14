def adjacency_lists():
    n, m = map(int, input().split())

    result = {}

    for k in range(m):
        v1, v2 = input().split()

        for v in v1, v2:
            if v not in result:
                result[v] = set()
        result[v1].add(v2)
        result[v2].add(v1)
    return result
