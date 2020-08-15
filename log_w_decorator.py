import logging
import time
from functools import wraps


def decorator_func(orig_func):
    def wrapper_func(*args, **kwargs):
        print('Wrapper_func runs before orig_func '
              'named: {}, with args: {}, kwargs: {}'.format(
               orig_func.__name__, args, kwargs))
        orig_func(*args, **kwargs)
    return wrapper_func


class decorator_class():
    def __init__(self, orig_func):
        self.orig_func = orig_func

    def __call__(self, *args, **kwargs):
        print('Call method runs before orig_func named: '
              f'{self.orig_func.__name__}')
        self.orig_func(*args, **kwargs)

@decorator_func
def display():
    print('display runs')


@decorator_func
def display_info(name, age):
    print(f'display_info runs with name: {name}, age: {age}')


display()
display_info('John', 29)
