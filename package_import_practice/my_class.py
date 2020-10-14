def func_1(): # function(in module)
    pass

class Person:
    def func_1(self):
        pass
    # class variables
    name = "女娲娘娘"
    age = 10000

    # private class variables
    __private_args = "class private"

    # def __init__(self):
    #     print('constructor called!')

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = "Male"
        print(self.name)
        print(self.age)
        print(self.gender)

    def get_private_args(self):
        print(self.__private_args)

    def __private_method(self):
        print("Private method called!")

    def _protected_method(self):
        print("protected method called!")

    @classmethod
    # cls is an abbreviation of class
    def my_class_method(cls):
        print(cls.name)
        print("class method!")

    @staticmethod
    def my_static_method():
        print("static method!")


# p = Person()
# print(p.name)
# print(p.age)
# print(p.__private_args)


p1 = Person("伏羲", 12000, "Male")
# print(p1.name)
# print(p1.age)
# print(p1.gender)

# calling static method
Person.my_static_method()
p1.my_static_method()

# calling class method
Person.my_class_method()
p1.my_class_method()

print(Person.__dict__)