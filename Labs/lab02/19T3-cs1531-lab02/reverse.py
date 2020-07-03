# Author: @abara15 (GitHub)

def reverse_words(string_list):
    '''
    Given a list of strings, return a new list where the order of the words is reversed.

    For example,
    >>> reverse_words(["Hello World", "I am here"])
    ['World Hello', 'here am I']
    '''
    new_string = []
    for i in string_list:
        revwords = i.split()
        revwords.reverse()
        revwords = ' '.join(revwords)
        new_string.append(revwords)
    return new_string

def test_one():
    l = ["Hello World", "I am here"]
    l = reverse_words(l)
    assert l == ["World Hello", "here am I"]

def test_two():
    l = ["My name", "is Anthony"]
    l = reverse_words(l)
    assert l == ["name My", "Anthony is"]

def test_three():
    l = ["COMP1531 is", "a fun subject"]
    l = reverse_words(l)
    assert l == ["is COMP1531", "subject fun a"]

def test_four():
    l = ["I am", "reversing words"]
    l = reverse_words(l)
    assert l == ["am I", "words reversing"]

def test_five():
    l = ["This will be my final test", "for my reverse function"]
    l = reverse_words(l)
    assert l == ["test final my be will This", "function reverse my for"]