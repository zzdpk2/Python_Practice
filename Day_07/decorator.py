# decorator


def func_1(x):
    return x * 2


def func_2(x):
    return x * 3


def func_3(x, y, i, j):
    return x(i) + y(j)


r = func_3(func_1, func_2, 2, 3)
print(r)

