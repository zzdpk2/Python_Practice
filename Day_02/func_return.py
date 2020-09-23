__author__ = "rex"
__date__ = "2020-09-23"


def func1():
    print("func1 called!")


f = func1()
print(f)
print(type(f))


def func2():
    return 'a'

f = func2()
print(f)
print(type(f))


def func3(x, y):
    z = x + y
    return z


f = func3(1, 2)
print(f)
print(type(f))


def func4():
    return 1, 2


x, y = func4()
print(x)
print(y)


# 函数的返回值是一个函数, 动态创建函数
def func5(x):
    if x == 2:
        def inner_func(y):
            print("inner 1 was called!")
            return y * y
    if x == 3:
        def inner_func(y):
            print("inner 2 was called!")
            return y * y * y
    else:
        def inner_func(y):
            print("inner was badly called!")
    return inner_func


calc = func5(2)
print(type(calc))
z = calc(4)
print(z)

