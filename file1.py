# Sieve of Eratosthenes

def sieve_of_Eratosthenes(n):
    """
    Prints prime numbers from 0 to n
    :param n: maximum prime number can be
    :return:
    """
    array = [True] * n

    array[0] = False
    array[1] = False
    for k in range(round(n ** 0.5) + 1):
        if array[k]:
            for j in range(2 * k, n, k):
                array[j] = False

    for k in range(n):
        if array[k]:
            print(k)


sieve_of_Eratosthenes(100)
