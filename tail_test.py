from tail import tail


def any_rec(iterable):
    '''
    >>> any_rec(0 for _ in range(10))
    False
    >>> any_rec(0 for _ in range(10000))
    Traceback (most recent call last):
    ...
    RecursionError: maximum recursion depth exceeded
    '''
    try:
        n = next(iterable)
    except StopIteration:
        return False
    return n or any_rec(iterable)


@tail
def any_tail(iterable):
    '''
    >>> any_tail(0 for _ in range(10000))
    False
    '''
    try:
        n = next(iterable)
    except StopIteration:
        return False
    return n or any_tail(iterable)
