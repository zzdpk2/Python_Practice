# class Father(object):
class Father:
    name = "Li Lei"
    gender = "Male"

    def __init__(self):
        print("Father constructor called!")

    def speak_english(self):
        print("Father speak english!")

    def __juehuo(self):
        print("Father juehuo")


class Mother:
    name = "Han Meimei"
    gender = "Female"

    def __init__(self):
        print("Mother constructor called!")

    def speak_chinese(self):
        print("Mother speaks Chinese!")


class Child(Father, Mother):
    def __init__(self):
        print("Child constructor called!")

    def speak_english(self):
        print("Child speaks English!")

    def study(self):
        print("Child study!")


c = Child()
c.speak_english()
c.speak_chinese()
print(Child.__bases__)
print(c.name)

