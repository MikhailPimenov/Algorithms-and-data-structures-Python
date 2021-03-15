def decorator_for_discrete_bag3(wrappee):
    def wrapper(items: tuple, mass):
        values = [items[i][1] for i in range(len(items))]
        masses = [items[i][0] for i in range(len(items))]
        return wrappee(values, masses, mass)

    return wrapper


@decorator_for_discrete_bag3
def discrete_bag3(values: tuple, masses: tuple, mass: int):
    f = [[0] * (len(values) + 1) for _ in range(mass + 1)]

    for i in range(1, mass + 1):
        for j in range(1, len(values) + 1):
            if masses[j - 1] <= i:
                f[i][j] = max(values[j - 1] + f[i - masses[j - 1]][j - 1], f[i][j - 1])
            else:
                f[i][j] = f[i][j - 1]

    return f[-1][-1]
