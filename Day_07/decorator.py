# decorator
import time


# def func_1(x):
#     return x * 2
#
#
# def func_2(x):
#     return x * 3
#
#
# def func_3(x, y, i, j):
#     return x(i) + y(j)
#
#
# r = func_3(func_1, func_2, 2, 3)
# print(r)


def runtime_noargs(function_name):
    def wrapper():
        start_time = time.time()
        function_name()
        end_time = time.time()
        print(end_time - start_time)
    return wrapper


@runtime_noargs
def function_demo1():
    print("demo1 is running!")


function_demo1()

