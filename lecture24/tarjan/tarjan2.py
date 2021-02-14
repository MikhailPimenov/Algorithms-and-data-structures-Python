# def decorator_catcher(function):
#     def wrapper(*args, **kwargs):
#         try:
#             result = function(*args, **kwargs)
#         except ArithmeticError:
#             print("Arithmetic error catched")
#         else:
#             return result
#
#     return wrapper
#
#
# @decorator_catcher
# def i_throw_exception(n: int):
#     if n < 0:
#         print("EXCEPTION")
#         raise ArithmeticError
#     else:
#         print("no exception")
#
#
# i_throw_exception(33)
# i_throw_exception(-2)

def catcher(function):
    def wrapper(*args,**kwargs):
        try:
            result = function(*args,**kwargs)
        except ArithmeticError:
            return False
        else:
            return result
    return wrapper


@catcher
def tarjan(graph: dict):
    gray_and_black = set()
    black = set()
    stack = []

    for v in graph:
        if v not in gray_and_black:
            depth_first_search(graph,v,gray_and_black,black,stack)

    number = 0
    numbers = {}

    while stack:
        numbers[stack.pop()] = number
        number += 1

    return numbers


def depth_first_search(graph: dict, start, gray_and_black: set, black: set, stack: list):
    gray_and_black.add(start)

    for n in graph[start]:
        if n not in gray_and_black:
            depth_first_search(graph, n, gray_and_black, black, stack)
        elif n not in black:
            raise ArithmeticError

    black.add(start)
    stack.append(start)
