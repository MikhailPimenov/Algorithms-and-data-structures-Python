def discrete_bag_adapter_decorator(wrappee):
    def wrapper(items: tuple, bag_mass: int):
        m = [None] * len(items)
        v = [None] * len(items)

        for i in range(len(items)):
            m[i] = items[i][0]
            v[i] = items[i][1]

        return wrappee(m, v, bag_mass)

    return wrapper


@discrete_bag_adapter_decorator
def discrete_bag4(m: list, v: list, bag_mass: int) -> int:
    ff = [[0 for _ in range(len(m) + 1)] for _ in range(bag_mass + 1)]

    for i in range(1, bag_mass + 1):
        for j in range(1, len(m) + 1):
            if i >= m[j - 1]:
                ff[i][j] = max(v[j - 1] + ff[i - m[j - 1]][j - 1], ff[i][j - 1])
            else:
                ff[i][j] = ff[i][j - 1]

    return ff[-1][-1]