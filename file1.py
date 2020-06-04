# lecture 13
# stack
# brace_sequence
# reverse_polish_notation

import A_stack


def brace_sequence(string: str):
    """
    Checks if brace sequence is correct
    :param string: sequence to check
    :return: True if sequence is correct, otherwise False
    >>> brace_sequence("()[]")
    True
    >>> brace_sequence("g[g(f()ff[])[f]ds()]")
    True
    >>> brace_sequence("ggf)f5")
    False
    >>> brace_sequence("fggf)f )g([])gf((")
    False
    >>> brace_sequence("](h)[ ][")
    False
    >>> brace_sequence("(  ]")
    False
    >>> brace_sequence("[(]tr)")
    False
    >>> brace_sequence("c ]v(v)vvv(v)f[")
    False
    >>> brace_sequence("5[4]3[f")
    False

    """

    b1o = "("
    b1c = ")"
    b2o = "["
    b2c = "]"

    stack = A_stack
    stack.clear()

    for index in range(len(string)):
        if string[index] == b1o or string[index] == b1c or string[index] == b2o or string[index] == b2c:
            if string[index] == b1c or string[index] == b2c:
                if stack.is_empty():  # there were NO opening braces before
                    return False
                else:  # there were opening braces before
                    if string[index] == b1c:
                        if stack.pop() != b1o:  # if opening brace does not match current closing brace:
                            return False
                    else:
                        if stack.pop() != b2o:
                            return False
            else:
                stack.push(string[index])

    return stack.is_empty()


def reverse_polish_notation(array: str):
    """
    Calculates expression given as reverse polish notation
    :param array: str as reverse polish notation to calculate
    :return: number as a calculated result
    >>> reverse_polish_notation("2,7, +")
    9
    >>> reverse_polish_notation("1,4,-")
    -3
    >>> reverse_polish_notation("5,8,*")
    40
    >>> reverse_polish_notation("100, 25, /")
    4.0

    """

    stack = A_stack
    stack.clear()

    index = 0
    while index < len(array):
        if array[index].isnumeric():
            number = int(array[index])
            k = 1
            while array[index + k].isnumeric():
                number *= 10
                number += int(array[index + k])
                k += 1
            stack.push(int(number))
            index += k
        elif array[index] == '+' or array[index] == '-' or array[index] == '*' or array[index] == '/':
            if not stack.is_empty():
                y = stack.pop()
            else:
                return -1
            if not stack.is_empty():
                x = stack.pop()
            else:
                return -1

            if array[index] == '+':
                stack.push(x + y)
            elif array[index] == '-':
                stack.push(x - y)
            elif array[index] == '*':
                stack.push(x * y)
            else:
                if not y == 0:
                    stack.push(x / y)
        index += 1

    return stack.pop()


reverse_polish_notation("2,7,+")

reverse_polish_notation("1,4,-")

reverse_polish_notation("5,8,*")

reverse_polish_notation("100, 25, /")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=False)
