# lecture 7
# gcd(a, b) - grand common divisor
# pow(a, b) 
# pow_fast(a, b)


def gcd(a, b):
    """
        Returns grand common divisor of a, b
        :param a: first of two numbers
        :param b: second of two numbers
        :return: grand common divisor
    """
    if a == b:
        return a

    elif a > b:
        return gcd(a - b, b)
    else:  # a < b
        return gcd(a, b - a)


def gcd2(a, b):
    """
        Returns grand common divisor of a, b
        :param a: first of two numbers
        :param b: second of two numbers
        :return: grand common divisor
    """
    return a if b == 0 else gcd2(b, a % b)


def pow(a, b):
    """

    :param a: base
    :param b: natural or zero number, power to base be set
    :return: base^power
    """
    if a < 0 or (b // 1) != b:
        print("b is not natural")
        return -1
    if b == 0:
        return 1
    # print("power = ", b)
    return a * pow(a, b - 1)


def pow_fast(a, b):
    """

    :param a: base
    :param b: natural or zero number, power to base be set
    :return: base^power
    """
    if a < 0 or (b // 1) != b:
        # print("b is not natural")
        return -1
    if b == 0:
        return 1
    # print("power fast = ", b)
    if b % 2 == 0:
        return pow_fast(a * a, b // 2)
    else:
        return a * pow_fast(a, b - 1)


def test_gcd(gcd_function, str=""):
    print(str)
    print("Test #1: ", "ok" if gcd_function(10, 15) == 5 else "FAILED")
    print("Test #2: ", "ok" if gcd_function(100, 15) == 5 else "FAILED")
    print("Test #3: ", "ok" if gcd_function(120, 15) == 15 else "FAILED")
    print("Test #4: ", "ok" if gcd_function(16, 40) == 8 else "FAILED")


def test_pow(pow_function, str=""):
    print(str)
    print("Test #1: ", "ok" if pow_function(2, 3) == 8 else "FAILED")
    print("Test #2: ", "ok" if pow_function(10, 2) == 100 else "FAILED")
    print("Test #3: ", "ok" if pow_function(2, 8) == 256 else "FAILED")
    print("Test #4: ", "ok" if pow_function(3, 3) == 27 else "FAILED")


test_gcd(gcd)
test_gcd(gcd2)
test_pow(pow, "Slow power:")
test_pow(pow_fast, "Fast power:")
