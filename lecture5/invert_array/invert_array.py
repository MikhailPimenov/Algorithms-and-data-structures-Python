def invert_array(A: list, N: int):
    if type(A) not in [list]:
        raise TypeError("wrong type of argument 1")
    if type(N) not in [int]:
        raise TypeError("wrong type of argument 2")
    for index in range(N // 2):
        A[index], A[N - 1 - index] = A[N - 1 - index], A[index]

    return A
