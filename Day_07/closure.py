# 简单来说，闭包就是外部函数的返回值是内部函数的引用


def outer(a):
    b = 10

    def inner():
        print(a + b)
    # 外部函数的返回值是内部函数的引用
    return inner


inner_func = outer(5)
print(type(inner_func))
inner_func()


