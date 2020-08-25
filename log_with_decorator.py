# import logging and timer modules to log and time functions
import logging
import timer
from functools import wraps


def logger_decor(orig_f):
    logging.basicConfig(filename='{}.log'.format(orig_f.__name__),
                        level=logging.INFO)
    @wraps()
    def wrapper(*args, **kwargs):
        logging.info(
            'The function ran with args: {}, and kwargs: {}'.format(args,
                                                                    kwargs)
        )
        return orig_f(*args, **kwargs)
    return wrapper

# This decorator calculates how long functions run.
def timer_decor(orig_f):
    @wraps()
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_f(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_f.__name__, t2))
        return result
    return wrapper

@logger_decor
def display(name, age):
    print('display func ran with arguments ({}, {})'.format(name, age))
