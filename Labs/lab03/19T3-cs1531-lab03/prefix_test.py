# Author: @abara15 (GitHub)
from prefix import prefix_search
import pytest

def test_documentation():
    assert prefix_search({"ac": 1, "ba": 2, "ab": 3}, "a") == { "ac": 1, "ab": 3}

def test_exact_match():
    assert prefix_search({"category": "math", "cat": "animal"}, "cat") == {"category": "math", "cat": "animal"}

def test_fail():
    with pytest.raises(KeyError, match=r'Prefix is not in dictionary.'):
        prefix_search({"cat": 3, "dog": 22, "lion" : 523}, "giraffe")

def test_documentation_2():
    assert prefix_search({"xyzabc": 1, "abxyz": 5, "xyz": 13}, "xyz") == { "xyzabc": 1, "xyz": 13}

def test_exact_match_2():
    assert prefix_search({"theme": "dark", "thesis": "none"}, "the") == {"theme": "dark", "thesis": "none"}
       
def test_fail_2():
    with pytest.raises(KeyError, match=r'Prefix is not in dictionary.'):
        prefix_search({"key1": 3, "key2": 22, "key3" : 523}, "key26")
