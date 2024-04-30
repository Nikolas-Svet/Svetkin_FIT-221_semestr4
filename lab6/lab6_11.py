class PowerSummator:

    def __init__(self, p):
        self.pow = p

    def transform(self):
        return self.pow

    def sum(self, N):
        return sum(n ** self.transform() for n in range(1, N + 1))


class SquareSummator(PowerSummator):

    def __init__(self, p):
        super().__init__(p)

    def transform(self):
        return self.pow


class CubeSummator(PowerSummator):

    def __init__(self, p):
        super().__init__(p)

    def transform(self):
        return self.pow


summator = PowerSummator(3.5)
square_summator = SquareSummator(2)
cube_summator = CubeSummator(3)

N = 5
print(f"Сумма первых {N} натуральных чисел: {summator.sum(N)} со степенью {summator.pow}")
print(f"Сумма квадратов первых {N} натуральных чисел: {square_summator.sum(N)} со степенью {square_summator.pow}")
print(f"Сумма кубов первых {N} натуральных чисел: {cube_summator.sum(N)} со степенью {cube_summator.pow}")
