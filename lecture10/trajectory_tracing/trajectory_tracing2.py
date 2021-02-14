def trajectory_tracing(value: list, allowed: list, n: int):
    if type(value) != list or type(allowed) != list or type(n) != int:
        raise TypeError

    if n != len(value) or n != len(allowed):
        raise ArithmeticError

    C = [0] * n
    C[0] = value[0]
    C[1] = (C[0] + value[1] if allowed[1] else float('+inf'))

    for cage in range(2, n):
        if allowed[cage]:
            C[cage] = value[cage] + min(C[cage - 1], C[cage - 2])
        else:
            C[cage] = float('+inf')

    return C[n - 1]
