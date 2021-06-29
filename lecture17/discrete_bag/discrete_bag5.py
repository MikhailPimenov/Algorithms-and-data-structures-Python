def discrete_bag5_adapter(wrappee):
    def wrapper(items: tuple, *args, **kwargs):
        m = [item[0] for item in items]
        v = [item[1] for item in items]

        return wrappee(m, v, *args, **kwargs)

    return wrapper


@discrete_bag5_adapter
def discrete_bag5(m: tuple, v: tuple, bag_mass: int) -> int:
    F = [[0 for _ in range(len(v) + 1)] for _ in range(bag_mass + 1)]

    for i in range(1, bag_mass + 1):
        for j in range(1, len(v) + 1):
            if i >= m[j - 1]:
                F[i][j] = max(v[j - 1] + F[i - m[j - 1]][j - 1], F[i][j - 1])
            else:
                F[i][j] = F[i][j - 1]

    return F[-1][-1]
