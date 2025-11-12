# https://github.com/andy-jpeg/lab11-AT-AV
# Partner 1: Andy Tran
# Partner 2: Augusto Valero

import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        result = b / a
        return result
    except ZeroDivisionError as error:
        print("Zero divsion error")

def log(a, b):
    try:
        result = math.log(a, b)
        return result
    except ValueError as error:
        print(error)

def exp(a, b):
    return a ** b