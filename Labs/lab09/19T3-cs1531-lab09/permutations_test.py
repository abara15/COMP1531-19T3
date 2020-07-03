# Author: @abara15 (GitHub)
from permutations import permutations
from hypothesis import given, strategies, assume
import inspect

def test_generator():
    '''
    Ensure it is generator function
    '''
    assert inspect.isgeneratorfunction(permutations), "permutations does not appear to be a generator"

def test_example1():
    assert sorted(list(permutations('ABC'))) == ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']

def test_example2():
    assert sorted(list(permutations('ABB'))) == ['ABB', 'ABB', 'BAB', 'BAB', 'BBA', 'BBA']

@given(strategies.text(min_size=1, max_size=25))
def test_property(n):
    prime_factors = list(permutations(n))
    for string in prime_factors:
        assert len(string) == len(n)