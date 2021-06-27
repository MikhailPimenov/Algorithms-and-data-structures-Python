def selection_sort5_adapter(wrappee):
    def wrapper(a: list):
        return wrappee(a, len(a))

    return wrapper


@selection_sort5_adapter
def selection_sort5(a: list, length: int):
    pass
