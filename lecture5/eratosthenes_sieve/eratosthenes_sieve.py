def eratosthenes_sieve(N: int):
    if type(N) not in [int, float]:
        raise TypeError
    if N < 0:
        raise ArithmeticError

    A = [True] * N
    for divisor in range(2, N // 2):
        for index in range(2 * divisor, N, divisor):
            A[index] = False

    for index in range(N):
        if A[index]:
            print(index)
