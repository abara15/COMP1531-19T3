# Author: @abara15 (GitHub)
from factors import factors, is_prime
from hypothesis import given, strategies
import inspect

def test_generator():
    '''
    Ensure it is generator function.
    '''
    assert inspect.isgeneratorfunction(factors), "factors does not appear to be a generator"

def test_36():
    assert list(factors(36)) == [2, 2, 3, 3]

def test_200():
    assert list(factors(200)) == [2, 2, 2, 5, 5]

def test_negative():
    assert list(factors(-90)) == []

def test_0():
    assert list(factors(0)) == []

def test_9876():
    assert list(factors(9876)) == [2, 2, 3, 823]

@given(strategies.integers(min_value=2, max_value=1000000))
def test_property(n):
    prime_factors = list(factors(n))
    product = 1
    for i in prime_factors:
        product *= i
    assert product == n