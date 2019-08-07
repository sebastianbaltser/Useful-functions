import time
"""func_timer.func_timer() prints elapsed time and results of function calls.
Use as decorator."""

def func_timer(func):
    def clocked(*args):
        start = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter()-start
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)

        print("[%.8fs] %s(%s) -> %r" % (elapsed, name, arg_str, result))
        return result
    return clocked

@func_timer
def test(a):
    return repr(a)

if __name__ == '__main__':
    test("test")
