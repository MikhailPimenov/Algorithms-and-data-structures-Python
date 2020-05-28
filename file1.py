# lecture 8
# generate_numbers
# generate_permutations


def generate_numbers(base: int, count: int = -1, prefix: list = None):
    """
    Generates all numbers with length count and base count system
    :param base: base of count system
    :param count: amount of symbols
    :param prefix: container for each result generated
    :return:
    """
    prefix = prefix or []

    if count == -1:
        count = base

    if count == 0:
        print(prefix)
        return

    for digit in range(base):
        prefix.append(digit)
        generate_numbers(base, count - 1, prefix)
        prefix.pop()


def find(element, array:list):
    for x in array:
        if x == element:
            return True
    return False


def generate_permutations(elements: list, count: int = -1, prefix: list = None):
    """
    Generates all possible count permutations of list elements
    :param elements: list of elements
    :param count: number of elements in one combination
    :param prefix: container of current combination
    :return:
    """

    prefix = prefix or [] # если этого не сделать, prefix нельзя будет использовать

    if count == -1:
        count = len(elements)

    if count == 0:
        print(prefix)
        return

    for x in elements:
        if not find(x, prefix):
            prefix.append(x)
            generate_permutations(elements, count - 1, prefix)
            prefix.pop()


generate_numbers(2)
generate_permutations([10, 20, 30, 40], 3)
