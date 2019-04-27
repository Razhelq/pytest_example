from ShpacooAlmanac.for_pytest import math_func
import pytest


@pytest.mark.parametrize('num1, num2, result',
                         [
                             (7, 3, 10),
                             ('Hello', ' World', 'Hello World'),
                             (10.5, 25.5, 36)
                         ]
                         )
def test_add(num1, num2, result):
    assert math_func.add(num1, num2) == result


@pytest.mark.parametrize('num1, num2, result',
                         [
                             (2, 3, 6),
                             ('Hello', 3, 'HelloHelloHello'),
                             (25, 4, 100)
                         ]
                         )
def test_product(num1, num2, result):
    assert math_func.product(num1, num2) == result
