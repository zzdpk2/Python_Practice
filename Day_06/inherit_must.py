from abc import ABCMeta, abstractclassmethod

class Tester(metaclass=ABCMeta):

    @abstractclassmethod
    def test(self):
        pass


class FunctionTester(Tester):
    def test(self):
        print("Function test called!")


f = FunctionTester()
f.test()

