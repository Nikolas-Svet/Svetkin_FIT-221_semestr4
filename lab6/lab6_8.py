base_symbol = " -> "


class Queue:
    base_symbol = " -> "

    def __init__(self, *args):
        self.arr = [*args]

    def __str__(self):
        return ''.join(map(str, [str(self.arr[i]) + base_symbol for i in range(len(self.arr) - 1)])) + str(self.arr[-1])

    def append(self, *args):
        for i in [*args]:
            self.arr.append(i)

    def pop(self):
        num = self.arr[0]
        del self.arr[0]
        return num

    def __add__(self, other):
        self.arr += other.arr
        return self.__str__()

    def extend(self, other):
        self.arr += other.arr

    def next(self):
        return Queue(*self.arr[1:])

    def copy(self):
        return Queue(*self.arr)

    def __eq__(self, other):
        return self.arr == other.arr


q1 = Queue(1, 2, 3)
print(q1)
q1.append(4, 5)
print(q1)
qx = q1.copy()
print(qx.pop())
print(qx)
q2 = q1.copy()
print(q2)
print(q1 == q2, id(q1) == id(q2))
q3 = q2.next()
print(q1, q2, q3, sep="\n")
print(q1 + q3)
q3.extend(Queue(1, 2))
print(q3)
q4 = Queue(1, 2)
# q4 += q3 >> 4