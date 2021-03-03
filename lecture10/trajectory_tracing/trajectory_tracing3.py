def trajectory_tracing3(prices: list, allowed: list, destination: int):
    if type(prices) not in [tuple, list]:
        raise TypeError
    if type(allowed) not in [tuple, list]:
        raise TypeError
    if type(destination) not in [int]:
        raise TypeError
    if len(prices) != len(allowed):
        raise ArithmeticError
    if destination > len(prices):
        raise ArithmeticError

    costs = [None] * len(prices)
    if allowed[0]:
        costs[0] = prices[0]
    if allowed[1]:
        costs[1] = prices[1] + (costs[0] if allowed[0] else 0)

    for k in range(2, destination):
        assert allowed[k - 1] or allowed[k - 2]
        if allowed[k - 1] and allowed[k - 2]:
            costs[k] = prices[k] + min(costs[k - 1], costs[k - 2])
        else:
            costs[k] = prices[k] + (costs[k - 1] if allowed[k - 1] else costs[k - 2])

    return costs[destination - 1]
