import functools


class _Delay:
    rec = 0

    def __init__(self, f, args, kwargs):
        self.f, self.args, self.kwargs = f, args, kwargs

    def __call__(self):
        _Delay.rec += 1
        try:
            return self.f(*self.args, **self.kwargs)
        finally:
            _Delay.rec -= 1


def tail(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        res = _Delay(f, args, kwargs)
        if _Delay.rec:
            return res
        while isinstance(res, _Delay):
            res = res()
        return res

    return wrapped
