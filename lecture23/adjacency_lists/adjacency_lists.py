def adjacency_lists():
    m, n = input().split()
    m = int(m)
    n = int(n)

    lists = dict()

    for k in range(n):
        v1, v2 = input().split()

        for v in v1, v2:
            if v not in lists:
                lists[v] = set()

        lists[v1].add(v2)
        lists[v2].add(v1)
    return lists