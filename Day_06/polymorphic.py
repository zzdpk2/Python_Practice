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


# person = Person()
# person.run()
# pig = Pig()
# pig.run()
# dog = Dog()
# dog.run()

"""
多态性
"""


def func(obj):
    obj.run()


person = Person()
pig = Pig()
dog = Dog()


func(person)
func(pig)
func(dog)


class Computer:
    def usb_insert(self):
        pass


def usb_run(sub_computer):
    sub_computer.usb_insert()


class Mouse(Computer):
    def usb_insert(self):
        print("Mouse inserted!")


class Keyboard(Computer):
    def usb_insert(self):
        print("Keyboard inserted!")

