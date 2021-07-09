def trajectory_tracing5(prices: tuple, allowed: tuple, destination: int) -> int:
    if type(prices) not in (list, tuple):
        raise TypeError
    if type(allowed) not in (list, tuple):
        raise TypeError
    if type(destination) != int:
        raise TypeError
    if destination > len(prices):
        raise ArithmeticError
    if len(prices) != len(allowed):
        raise ArithmeticError

    F = [0] * len(prices)

    if allowed[0]:
        F[0] = prices[0]
    if allowed[1]:
        F[1] = F[0] + prices[1]

    for i in range(2, len(prices)):
        if allowed[i - 1] and allowed[i - 2]:
            F[i] = prices[i] + (F[i - 1] if F[i - 1] < F[i - 2] else F[i - 2])
        elif allowed[i - 1]:
            F[i] = prices[i] + F[i - 1]
        elif allowed[i - 2]:
            F[i] = prices[i] + F[i - 2]

    return F[destination - 1]
