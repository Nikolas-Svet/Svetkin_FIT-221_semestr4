print("\nПервое")


class BigBell:
    def __init__(self):
        self.flag = True

    def sound(self):
        if self.flag:
            print("ding")
            self.flag = False
        else:
            print("dong")
            self.flag = True


bell = BigBell()
bell.sound()
bell.sound()
bell.sound()

print("\nВторое")


class Balance:
    def __init__(self):
        self.left_weight = 0
        self.right_weight = 0

    def add_left(self, num):
        self.left_weight += num

    def add_right(self, num):
        self.right_weight += num

    def result(self):
        if self.left_weight == self.right_weight:
            return "="
        elif self.left_weight > self.right_weight:
            return "L"
        else:
            return "R"


balance = Balance()
balance.add_right(10)
balance.add_left(9)
balance.add_left(2)
print(balance.result())
balance.add_right(1)
print(balance.result())
balance.add_right(10)
print(balance.result())

print("\nТретье")


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

print("\nЧетвертое")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __ne__(self, other):
        return not self.__eq__(other)


# Пример использования
point1 = Point(3, 4)
point2 = Point(3, 4)
point3 = Point(5, 6)

print(point1 == point2)
print(point1 != point2)
print(point1 == point3)
print(point1 != point3)

print("\nПятое")


class ReversedList:

    def __init__(self, array_num):
        self.array_num = array_num

    def __len__(self):
        return len(self.array_num)

    def __getitem__(self, item):
        return self.array_num[-1::-1][item]


rlist = ReversedList([1, 2, 3, 4, 5])
for i in range(len(rlist)):
    print(rlist[i])

print("\nШестое")


class SparseArray:
    def __init__(self):
        self.data = {}

    def __setitem__(self, index, value):
        if value != 0:
            self.data[index] = value

    def __getitem__(self, index):
        return self.data.get(index, 0)


arr = SparseArray()
arr[1] = 10
arr[3] = 20
arr[5] = 0
print(arr[1])
for i in range(8):
    print(arr[i])

print("\nСедьмое")


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

print("\nВосьмое")

base_symbol = " -> "


class Queue:
    # base_symbol = " -> "
    def __init__(self, *args):
        self.arr = [*args]

    def __str__(self):
        return ''.join(map(str, [str(self.arr[i]) + base_symbol for i in range(len(self.arr) - 1)])) + str(self.arr[-1])

    def append(self, *args):
        for i in [*args]:
            self.arr.append(i)
        print(self.arr)

    def pop(self):
        num = self.arr[0]
        del self.arr[0]
        return num

    # def copy(self):




q1 = Queue(1, 2, 3)
print(q1)
q1.append(4, 5)
print(q1)
# print(q1.pop())
