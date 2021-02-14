def discrete_bag(items: list, M: int):
    ms = [items[k][0] for k in range(len(items))]
    vs = [items[k][1] for k in range(len(items))]

    f = [[0] * (M + 1) for k in range(len(vs) + 1)]

    for i in range(1, len(vs) + 1):
        for m in range(1, M + 1):
            if m - ms[i - 1] >= 0:
                f[i][m] = max(f[i - 1][m - ms[i - 1]] + vs[i - 1], f[i - 1][m])
    return f[len(vs)][M]
