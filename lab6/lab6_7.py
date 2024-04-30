class Polynomial:
    def __init__(self, *args):
        self.list_num = [*args]

    def __call__(self, x):
        y = self.list_num[0]

        for i in range(len(self.list_num)):
            if i == 0:
                continue
            y += self.list_num[i] * x ** i

        return y


poly = Polynomial(10, -1)

print(poly(0))
print(poly(1))
print(poly(2))