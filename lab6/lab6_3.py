class Selector:
    def __init__(self, arr_num):
        self.arr_num = arr_num

    def get_odds(self):
        return [i for i in self.arr_num if i % 2 != 0]

    def get_evens(self):
        return [i for i in self.arr_num if i % 2 == 0]


selector = Selector([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
odds = selector.get_odds()
evens = selector.get_evens()
print(*odds)
print(*evens)