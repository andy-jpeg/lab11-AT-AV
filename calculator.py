# https://github.com/andy-jpeg/lab11-AT-AV
# Partner 1: Andy Tran
# Partner 2: Augusto Valero

import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    result = b / a

    if a == 0:
        raise ZeroDivisionError

    return result

def logarithm(a, b):
    result = math.log(a, b)

    if b == 0:
        raise ValueError

    return result

def exp(a, b):
    return a ** b

def square_root(a):
    result = math.sqrt(a)
    return result

def hypotenuse(a, b):
    return math.hypot(a, b)