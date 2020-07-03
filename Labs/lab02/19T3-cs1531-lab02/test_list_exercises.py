# Author: @abara15 (GitHub)
from list_exercises import *

def test_reverse():
    l = [0]
    reverse_list(l)
    assert l == [0]

    l = [-3, -2, -1, 0, 1, 2, 3]
    reverse_list(l)
    assert l == [3, 2, 1, 0, -1, -2, -3]

    # TODO Write more tests for reverse
    # Test 1
    l1 = [0]
    reverse_list(l1)
    assert l1 == [0]

    l1 = [3, 2, 6, 19, 0, 21]
    reverse_list(l1)
    assert l1 == [21, 0, 19, 6, 2, 3]

    # Test 2
    l2 = [0]
    reverse_list(l2)
    assert l2 == [0]

    l2 = [-8, 1, -945, 1865, 12]
    reverse_list(l2)
    assert l2 == [12, 1865, -945, 1, -8]

def test_min():
    assert minimum([0]) == 0
    assert minimum([-3, -2, -1, 0, 1, 2, 3]) == -3
    # TODO Write more tests for minimum
    # Test 1
    assert minimum([0]) == 0
    assert minimum([9, 4, -9, -900, -899]) == -900

    # Test 2
    assert minimum([0]) == 0
    assert minimum([1981243, -5, 213123, 1, 0, -5]) == -5
    

def test_sum():
    assert sum_list([0]) == 0
    assert sum_list([-3, -2, -1, 0, 1, 2, 3]) == 0
    # TODO Write more tests for sum
    # Test 1
    assert sum_list([0]) == 0
    assert sum_list([9, 18, 27, 36, 45, -9]) == 126

    # Test 2
    assert sum_list([0]) == 0
    assert sum_list([-5, -4, -3, -2, -1, 15]) == 0
