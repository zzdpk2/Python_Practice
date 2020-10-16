class A(object):
    def test(self):
        print("Class A")


class B(A):
    # def test(self):
    #     print("Class B")
    pass


class C(A):
    def test(self):
        print("Class C")


class D(B):
    # def test(self):
    #     print("Class D")
    pass


class E(C):
    def test(self):
        print("Class E")


class F(D, E):
    # def test(self):
    #     print("Class F")
    pass


f = F()
f.test()

print(F.__mro__)


# (<class '__main__.F'>, <class '__main__.D'>, <class '__main__.B'>, <class '__main__.E'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
# F --> D -->B --> E --> C --> A

