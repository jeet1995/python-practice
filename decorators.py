# nested function definition
def func_outer():
    print('Hello from the outer most function')

    def func_inner_one():
        return '\tHello from the first inner function'

    print(func_inner_one())


# returning functions
def func_with_return_func(flag='first'):
    def func_first():
        return 'Hello from the first inner function'

    def func_second():
        return 'Hello from the second inner function'

    if flag == 'first':
        return func_first()
    else:
        return func_second()


# defining a decorator
def new_decorator(original_func):
    def wrapper_func():
        print('Some extra code before the function')
        original_func()
        print('Some extra code after the function')

    return wrapper_func


@new_decorator
def i_want_to_be_decorated_func():
    print('I want to be decorated')


if __name__ == '__main__':
    func_outer()
    print(func_with_return_func())
    print(func_with_return_func('second'))
    decorated_func = new_decorator(i_want_to_be_decorated_func)
    decorated_func()
    i_want_to_be_decorated_func()
