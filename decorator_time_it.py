import time
import functools


def my_timer(orig_f):

    @functools.wraps(orig_f)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = orig_f(*args, **kwargs)
        end = time.perf_counter() - start
        print(f'The function {orig_f.__name__!r} run in {end:.6f} sec')
        return result
    return wrapper


@my_timer
def my_func(n):
    my_list = []
    for i in range(n):
        my_list.append(i**2)
    return d


my_func(100)
