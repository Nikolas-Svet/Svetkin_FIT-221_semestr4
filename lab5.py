from functools import reduce

print("\nПервое")

l = [1, 2, 3, 4, 5, 6, 7, 8, 70, 4, 5]
print(*filter(lambda x: x < 5, l))
print(*map(lambda x: x / 2, l))
print(*(i / 2 for i in filter(lambda x: x > 17, l)))
l = [12, 27, 32, 45, 51, 61, 72, 81, 70, 4, 5]
print(sum(i ** 2 for i in filter(lambda x: x % 9 == 0, l)))

print("\nВторое")


def factorials(n):
    result = 1
    for k in range(1, n + 1):
        result *= k
        yield result


n = int(input("Factorial number: "))
for factorial in factorials(n):
    print(factorial, end=" ")

print("\nТретье")


def square_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib_gen = square_fibonacci()
for _ in range(10):  # Получить первые 10 чисел Фибоначчи
    print(next(fib_gen), end=" ")

print("\nЧетвертое")


def russian_alphabet():
    ord_a = ord('а')
    ord_ya = ord('я')
    current_ord = ord_a
    while current_ord <= ord_ya:
        yield chr(current_ord)
        current_ord += 1


for letter in russian_alphabet():
    print(letter, end=" ")

print("\nПятое")

russian_alphabet = (chr(i) for i in range(ord('а'), ord('я') + 1))

# Использование генераторного выражения для вывода букв русского алфавита
for letter in russian_alphabet:
    print(letter, end=" ")

print("\nШестое")


def arithmetic_operation(operation):
    if operation == '+':
        return lambda x, y: x + y
    elif operation == '-':
        return lambda x, y: x - y
    elif operation == '*':
        return lambda x, y: x * y
    elif operation == '/':
        return lambda x, y: x / y
    else:
        return None


# Пример использования:
operation = arithmetic_operation('+')
print(operation(1, 4))  # Вывод: 5

print("\nСедьмое")


def same_by(characteristic, objects):
    if not objects:
        return True
    characteristic_values = [characteristic(obj) for obj in objects]
    return all(value == characteristic_values[0] for value in characteristic_values)


# Пример использования:
values = [2, 2, 10, 61]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')

print("\nВосьмое")


def print_operation_table(operation, num_rows=9, num_columns=9):
    # Вывод заголовка таблицы
    print("    ", end="")
    for col in range(1, num_columns + 1):
        print(f"{col:4}", end="")
    print("\n" + "   " + "----" * num_columns)

    # Вывод значений таблицы
    for row in range(1, num_rows + 1):
        print(f"{row:2} |", end="")
        for col in range(1, num_columns + 1):
            print(f"{operation(row, col):4}", end="")
        print()


# Пример использования:
def multiplication_table(row, col):
    return row * col


print_operation_table(multiplication_table, num_rows=9, num_columns=9)

print("\nДесятое")

words = input().split()  # Ввод строки и разделение на слова
sorted_words = sorted(words, key=str.lower)  # Сортировка слов без учета регистра
print(' '.join(sorted_words))  # Вывод отсортированных слов в исходном регистре

print("\nОдиннадцатое")

# Пример последовательности целых чисел
numbers = [5, -3, 10, -7, 2]

# Сортировка по убыванию модуля числа
sorted_numbers = sorted(numbers, key=abs, reverse=True)

print(sorted_numbers)

print("\nДвенадцатое")

# Заданные координаты точек
points = [(1, 2), (-3, 4), (5, -6), (-7, -8), (1, -2)]


# Функция для вычисления расстояния от точки до начала координат
def distance(point):
    return (point[0] ** 2 + point[1] ** 2) ** 0.5


# Сортировка точек по удалению от начала координат
sorted_points = sorted(points, key=lambda point: (distance(point), point[0], point[1]))

print(sorted_points)
