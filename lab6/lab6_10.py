class Summator:
    def transform(self, n):
        return n

    def sum(self, N):
        return sum(self.transform(n) for n in range(1, N + 1))


class SquareSummator(Summator):
    def transform(self, n):
        return n ** 2


class CubeSummator(Summator):
    def transform(self, n):
        return n ** 3


summator = Summator()
square_summator = SquareSummator()
cube_summator = CubeSummator()

N = 5
print(f"Сумма первых {N} натуральных чисел: {summator.sum(N)}")
print(f"Сумма квадратов первых {N} натуральных чисел: {square_summator.sum(N)}")
print(f"Сумма кубов первых {N} натуральных чисел: {cube_summator.sum(N)}")
