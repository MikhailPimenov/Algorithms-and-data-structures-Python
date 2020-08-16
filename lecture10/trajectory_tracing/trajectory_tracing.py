def trajectory_tracing(prices: list, allowed: list, destination: int):
    if type(prices) not in [list]:
        raise TypeError
    if type(allowed) not in [list]:
        raise TypeError
    if type(destination) not in [int]:
        raise TypeError

    if len(prices) != len(allowed):
        raise ArithmeticError
    if destination > len(prices):
        raise ArithmeticError

    cost = [0 for k in range(len(prices))]
    cost[0] = prices[0]
    cost[1] = prices[1]

    for k in range(2, len(cost)):
        if allowed[k]:
            if not allowed[k - 1] and not allowed[k - 2]:
                raise ArithmeticError
            elif allowed[k - 1] and allowed[k - 2]:
                cost[k] = min(cost[k - 1], cost[k - 2]) + prices[k]
            elif allowed[k - 1] and not allowed[k - 2]:
                cost[k] = cost[k - 1] + prices[k]
            elif allowed[k - 2] and not allowed[k - 1]:
                cost[k] = cost[k - 2] + prices[k]

    return cost[destination - 1]
