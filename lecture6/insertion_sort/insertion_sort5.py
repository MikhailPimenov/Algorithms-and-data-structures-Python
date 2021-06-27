def insertion_sort5_adapter(wrappee):
    def wrapper(a: list):
        return wrappee(a, len(a))

    return wrapper


@insertion_sort5_adapter
def insertion_sort5(a: list, length: int):
    for i in range(1, length):
        for k in reversed(range(1, i + 1)):
            if a[k - 1] > a[k]:
                a[k - 1], a[k] = a[k], a[k - 1]
            else:
                break
