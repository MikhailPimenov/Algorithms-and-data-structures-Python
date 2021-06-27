def bubble_sort5_adapter(wrappee):
    def wrapper(a: list):
        return wrappee(a, len(a))

    return wrapper


@bubble_sort5_adapter
def bubble_sort5(a: list, length: int):
    for i in reversed(range(length)):
        go_on = False

        for j in range(length - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                go_on = True

        if not go_on:
            break
