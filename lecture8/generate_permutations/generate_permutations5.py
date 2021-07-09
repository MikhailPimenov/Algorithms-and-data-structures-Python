def generate_permutations5(items: list, n: int) -> None:
    if type(items) not in (list, tuple, set, dict):
        raise TypeError
    if type(n) != int:
        raise TypeError

    prefix = []
    return generate_permutations_recursive(items, prefix, n)


def generate_permutations_recursive(items: list, prefix: list, n: int) -> None:
    if not n:
        print(prefix)
        return

    for item in items:
        prefix.append(item)
        generate_permutations_recursive(items, prefix, n - 1)
        prefix.pop()
