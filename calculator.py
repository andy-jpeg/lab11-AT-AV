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
    try:
        result = b / a
        return result
    except ZeroDivisionError as error:
        print("Zero division error")

def logarithm(a, b):
    try:
        result = math.log(a, b)
        return result
    except ValueError as error:
        print(error)

def exp(a, b):
    return a ** b

def square_root(a):
    try:
        result = math.sqrt(a)
        return result
    except ValueError as error:
        print(error)

def hypotenuse(a, b):
    return math.hypot(a, b)