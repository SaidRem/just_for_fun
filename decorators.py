
# Decorate with function.
# Decorator wraps a function and changes its behavior.
def decorator_func(orig_func):
    def wrapper_func(*args, **kwargs):
        print('Wrapper_func runs before orig_func '
              'named: {}, with args: {}, kwargs: {}'.format(
               orig_func.__name__, args, kwargs))
        orig_func(*args, **kwargs)
    return wrapper_func

# Decorate with class.
class decorator_class():
    def __init__(self, orig_func):
        self.orig_func = orig_func

    def __call__(self, *args, **kwargs):
        print('Call method runs before orig_func named: '
              f'{self.orig_func.__name__}')
        self.orig_func(*args, **kwargs)

# Decorate function with function decorator.
@decorator_func
def display():
    print('display runs')

# Decorate function with class decorator.
@decorator_class
def display_info(name, age):
    print(f'display_info runs with name: {name}, age: {age}')


display()
display_info('John', 29)
