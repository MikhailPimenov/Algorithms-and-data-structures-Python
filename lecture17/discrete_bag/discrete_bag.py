def discrete_bag(items: list, mass: int) -> int:
    cost = [[0] * (len(items) + 1) for m in range(mass + 1)]

    for i in range(1, len(items) + 1):
        for m in range(mass + 1):
            if items[i - 1][0] <= m:
                cost[m][i] = max(items[i - 1][1] + cost[m - items[i - 1][0]][i - 1], cost[m][i - 1])
            else:
                cost[m][i] = cost[m][i - 1]
    return cost[mass][len(items)]
