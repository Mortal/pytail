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


@tail
def fac(n, a=1):
    '''
    >>> fac(5)
    120
    >>> from math import factorial
    >>> fac(10000) == factorial(10000)
    True
    '''
    return a if n == 0 else fac(n-1, a*n)
