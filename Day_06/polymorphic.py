"""
多态
多态指一类事物有多种形态
多态性
多态 不等于 多态性
"""


class Animal:
    def run(self):
        raise AttributeError("子类必须实现这个方法")


class Person(Animal):
    def run(self):
        print("人走")


class Pig(Animal):
    def run(self):
        print("猪跑")


class Dog(Animal):
    def run(self):
        print("狗跑")


p = Person()
p.run()

