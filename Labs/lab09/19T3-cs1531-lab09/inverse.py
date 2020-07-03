# Author: @abara15 (GitHub)
def inverse(d):
    '''
    Given a dictionary d, invert its structure such that values in d map to lists of keys in d. For example:
    >>> inverse({1: 'A', 2: 'B', 3: 'A'})
    {'A': [1, 3], 'B': [2]}
    '''
    inverted_dict = dict()
    for key, value in d.items():
        inverted_dict.setdefault(value, list()).append(key)
    
    return inverted_dict

    pass