def generate_permutations3(items: list, length: int):
    if type(length) not in [int]:
        raise TypeError
    if type(items) not in [list, dict, set]:
        raise TypeError

    prefix = []
    for current_length in range(1, length + 1):
        generate_permutations_recursive3(items, current_length, prefix)


def generate_permutations_recursive3(items: list, length: int, prefix: list):
    if length < 1:
        print(prefix)
        return

    for item in items:
        if item not in prefix:
            prefix.append(item)
            generate_permutations_recursive3(items, length - 1, prefix)
            prefix.pop()
