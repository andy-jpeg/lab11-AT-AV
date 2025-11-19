# https://github.com/andy-jpeg/lab11-AT-AV
# Partner 1: Andy Tran
# Partner 2: Augusto Valero


from calculator import *


def test_add():
    assert add(3, 6)== 9
    assert add(-4, -7) == -11
    assert add(-2, 5 ) == 3
    assert add(0, 0) ==0

def test_subtract():
    assert substract(9, 3)== 6
    assert substract(5, -3)== 8
    assert substract(4, -6) == -2
    assert substract(-1, -1)== -2


def test_divide_by_zero():
    try:
        div(0,10)
        assert False, "ZeroDivisionError was not raised for div(0, 10)"
    except ZeroDivisionError:
        pass

def test_logarithm():

    result1 = logarithm(10, 100)
    assert result1 == 2


    result2 = logarithm(2, 8)
    assert result2 == 3



def test_log_invalid_base():
    invalid_cases = [
        (1, 10),
        (0, 10),
        (-2, 8),
        (10, 0),
        (10, -5),
    ]

    for a, b in invalid_cases:
        try:
            logarithm(a, b)

            assert False, f"ValueError was not raised for log({a}, {b})"
        except ValueError:
            pass


