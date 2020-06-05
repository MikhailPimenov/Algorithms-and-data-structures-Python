# lecture 17
# fibbonachi_recursive_cash
# descrete_bag

cash = [0] * 10000


def fibbonachi_recursive_cash(n: int):
    """
    Returns fibbonachi number n using recursion with cash
    :param n: number of fibbonachi to return
    :return: number
    """

    if n > 10000:
        return -1

    if 0 <= n <= 1:
        if cash[n] == 0:
            cash[n] = n
        return cash[n]

    if cash[n] == 0:
        cash[n] = fibbonachi_recursive_cash(n - 1) + fibbonachi_recursive_cash(n - 2)

    return cash[n - 1] + cash[n - 2]


def discrete_bag(mass: list, price: list, mass_limit: int):
    """
    Returns maximum cost of items with limited sum mass
    :param mass: list of masses
    :param price: list of prices
    :param mass_limit: int, limit of sum mass
    :return: int
    """

    cost = [[0] * (len(mass) + 1) for m in range(mass_limit + 1)]

    for i in range(len(mass) + 1):
        for m in range(mass_limit + 1):
            if m - mass[i - 1] >= 0:
                cost[m][i] = max(price[i - 1] + cost[m - mass[i - 1]][i - 1], cost[m][i - 1])
            else:
                cost[m][i] = cost[m][i - 1]

    return cost[mass_limit][len(mass)]


def test_fibbonachi_recursive_cash():
    print("testing fibbonachi:")

    for k in range(20):
        print(k, fibbonachi_recursive_cash(k))


# test_fibbonachi_recursive_cash()
def test_discrete_bag(algorithm):
    print("testing discrete_bag")
    max_mass = 10

    mass = [3, 3, 4, 5]
    price = [30, 30, 40, 50]
    print("test #1:", "ok" if algorithm(mass, price, max_mass) == 100 else "FAILED")

    mass = [4, 9, 5, 4]
    price = [30, 50, 40, 20]
    print("test #2:", "ok" if algorithm(mass, price, max_mass) == 70 else "FAILED")

    mass = [5, 4, 3, 2]
    price = [200, 160, 110, 70]
    print("test #3:", "ok" if algorithm(mass, price, max_mass) == 380 else "FAILED")


test_discrete_bag(discrete_bag)
