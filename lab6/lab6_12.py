class A:
    def hello(self):
        print("Hello")

    def __str__(self):
        return "A.__str__ method"


class B(A):

    def __str__(self):
        return "B.__str__ method"

    def good_evening(self):
        print("Good evening")


class C(B, A):
    def __str__(self):
        return A.__str__(self)

class D(B, A):
    pass


c = C()
c.hello()
c.good_evening()
d = D()
d.hello()
d.good_evening()
print(c)
print(d)
