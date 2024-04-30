from math import *


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetr(self):
        p = (self.a + self.b + self.c) / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


class EquilateralTriangle(Triangle):

    def __init__(self, a):
        super().__init__(a, a, a)


et = EquilateralTriangle(4)
t = Triangle(3, 4, 5)

print(et.perimetr())
print(t.perimetr())