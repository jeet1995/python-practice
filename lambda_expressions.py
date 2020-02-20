
higher_order_func = lambda x, func: x + func(x)

if __name__ == '__main__':
    sum_func = (lambda x, y: x + y)
    _sum = sum_func(7, 3)
    print(_sum)
    print(higher_order_func(2, lambda x: x**2))
    print(higher_order_func(3, lambda x: x + 3))