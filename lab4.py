print("\nПервое")

my_list = [3, 5, 2, 32, 6, 1, 4, -5, 3, 1, 4, 43, 121]

my_list_2 = [i for i in my_list if i < 5]
print(my_list_2)

my_list_2 = [i / 2 for i in my_list]
print(my_list_2)

my_list_2 = [i * 2 for i in my_list if i > 17]
print(my_list_2)

my_list_2 = [i * i for i in range(0, int(input("Введите число: ")) + 1)]
print(my_list_2)

my_list_2 = [int(i) ** 2 for i in range(len(input("Введите список чисел: ").split()) + 1)]
print(my_list_2)

print([int(i) ** 2 for i in input("Введите список чисел: ").split() if (int(i) % 2 != 0 and (int(i) ** 2) % 10 != 9)])

print("\nВторое")

print(*map(lambda x: ('*' * x), map(int, input('->').split())), sep='\n')

print("\nТретье")


def triangle(a, b, c):
    if sorted([a, b, c])[0] + sorted([a, b, c])[1] > sorted([a, b, c])[2]:
        print("Это треугольник")
    else:
        print("Это не треугольник")


triangle(20, 13, 17)

print("\nЧетвертое")

import math


def distance(x1, y1, x2, y2):
    print(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))


distance(1, 2, 4, 6)

print("\nПятое")


def number_to_words(n):
    units = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
             6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
    tens = {2: 'двадцать', 3: 'тридцать', 4: 'сорок', 5: 'пятьдесят',
            6: 'шестьдесят', 7: 'семьдесят', 8: 'восемьдесят', 9: 'девяносто'}
    teens = {10: 'десять', 11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать',
             14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать', 17: 'семнадцать',
             18: 'восемнадцать', 19: 'девятнадцать'}

    if n < 1 or n > 99:
        return "Число должно быть от 1 до 99"

    if n in units:
        return units[n]
    elif n in tens:
        return tens[n]
    elif n in teens:
        return teens[n]
    else:
        tens_digit = n // 10
        units_digit = n % 10
        return tens[tens_digit] + ' ' + units[units_digit]


print(number_to_words(int(input("Введите число: "))))

print("\nШестое")


def bracket_check(s):
    stack = []
    mapping = {')': '('}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return "YES" if not stack else "NO"


print(bracket_check("()()()()()"))

print("\nСедьмое")


def palindrome(s):
    s = s.lower().replace(" ", "")
    if s == s[::-1]:
        print("Палиндром")
    else:
        print("Не палиндром")


palindrome("А роза упала на лапу Азора")
palindrome("Палиндром")

print("\nВосьмое")


def tic_tac_toe(field):
    if ['x', 'x', 'x'] in field and ['0', '0', '0'] in field:
        print("Быть не может")
        return
    for line in field:
        if ['x', 'x', 'x'] == line or ['0', '0', '0'] == line:
            print(line[0] + " win")
            return
    for i in range(3):
        if field[0][i] == field[1][i] == field[2][i] and (field[0][i] == 'x' or field[0][i] == '0'):
            print(field[0][i] + " win")
            return
    if field[0][0] == field[1][1] == field[2][2] or field[0][2] == field[1][1] == field[2][0]:
        print(field[1][1] + " win")
        return
    print("Draw")


# Пример ввода для 3x3 крестики-нолики
print("Введите игровое поле (по одной строке):")
field = []
for _ in range(3):
    row = input().split()
    field.append(row)

tic_tac_toe(field)

print("\nДевятое")

x = ""


def print_without_duplicates(s):
    global x
    if x != s:
        print(s)
        x = s
        return
    else:
        return


print_without_duplicates("Привет")
print_without_duplicates("Не могу до тебя дозваониться")
print_without_duplicates("Не могу до тебя дозваониться")
print_without_duplicates("Не могу до тебя дозваониться")
print_without_duplicates("Когда доедешь до дома")
print_without_duplicates("Ага, жду")

print("\nДесятое")

d = dict()


def add_friend(name_of_person, list_of_friends):
    global d
    if name_of_person in d.keys():
        if len(list_of_friends) == 1 or isinstance(list_of_friends, str):
            d[name_of_person].append(list_of_friends)
        else:
            for i in list_of_friends:
                d[name_of_person].append(i)
    else:
        d[name_of_person] = list_of_friends


def are_friends(name_of_preson1, name_of_person2):
    global d
    list_of_friends1 = d[name_of_preson1]
    for i in list_of_friends1:
        if i == name_of_person2:
            print(True)
            return
    print(False)
    return


def print_friends(name_of_person):
    global d
    print(" ".join([i for i in d[name_of_person]]))


add_friend("Алла", ["Марина", "Иван"])
are_friends("Алла", "Мария")
add_friend("Алла", "Мария")
are_friends("Алла", "Мария")
print_friends("Алла")

print("\nОдинадцатое")

one = 3
two = 2
three = 0


def to_roman(n):
    roman_numerals = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X',
        40: 'XL', 50: 'L', 90: 'XC', 100: 'C',
        400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
    }
    result = ''
    for value, numeral in sorted(roman_numerals.items(), reverse=True):
        while n >= value:
            result += numeral
            n -= value
    return result


def round():
    global one, two, three
    three = one + two
    print(to_roman(one) + " + " + to_roman(two) + " = " + to_roman(three))


round()

print("\nДвенадцатое")

# Пример, когда результаты одинаковы

value = 5
addition = 3

value += addition

print("Результат после использования оператора '+=':", value)  # 8

value = value + addition

print("Результат после использования оператора '+':", value)  # 11

# Оператор value = value + addition создает новый объект после сложения
# и затем присваивает его переменной value. Это может быть неэффективно,
# особенно при работе с большими объектами.
#
# Оператор value += addition выполняет то же самое сложение и присваивание,
# но, если это возможно, он изменяет существующий объект, чтобы избежать
# создания нового. Это может быть более эффективным, особенно при работе с
# изменяемыми объектами, такими как списки или словари.


print("\nТринадцатое")

# Здесь функция sort() применяется к списку arr, но переменной sorted_arr
# присваивается результат вызова функции sort(), который является None,
# так как sort() изменяет список на месте и не возвращает новый отсортированный список

arr = ['banana', 'apple', 'orange']
sorted_arr = arr.sort()
print("Отсортированный список:", sorted_arr)
print("Исходный список:", arr)

# В свою очередь функция sorted() применяется при выводе, но не сохраняет
# отсортированный список в переменную, а возвращает результат там, где
# вызывалась данная функция
arr = ['banana', 'apple', 'orange']
print(sorted(arr))
print(arr)

print("\nЧетырнадцатое")

# Ошибка в инициализации списков odd и even, они на самом деле являются ссылками
# на один и тот же список. Это означает, что при добавлении чисел в список, они
# добавляются в один и тот же список, а не в два отдельных.

# Исправленный вид кода

numbers = [2, 5, 7, 7, 8, 4, 1, 6]
odd = []
even = []
for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

print("\nПятнадцатое")

# Исходный список
fractal = [1, 3, 5, 7]

# Создаем фрактальный список

fractal.append(fractal)
fractal.append(fractal)
del fractal[1:4]
fractal[0] = 0
fractal.append(2)

# Печать фрактального списка
print(fractal)

print("\nШестнадцатое")
# Ошибка заключается в том, что глобальная переменная никак не была связана с функцией.
# Переменная передавала свое значение, а в функции создавалась лоакьльная с таким же именем
# и значением
sequence = [1, 1]


def continue_fibonacci_sequence(n):
    global sequence
    for i in range(n):
        next_element = sequence[-1] + sequence[-2]
        sequence = sequence + [next_element]


continue_fibonacci_sequence(1)
print(*sequence)

print("\nСемнадцатое")
arr = [1, 2]


def mirror():
    global arr
    mirrored_part = arr[::-1]
    arr = arr + mirrored_part


mirror()
print(*arr)

print("\nВосемнадцатое")

a = [1, 2, 3]


def from_string_to_list(string, container):
    global a  # Объявляем a как глобальную переменную
    a = container + [int(i) for i in string.split()]  # Обновляем значение глобальной переменной


from_string_to_list("1 3 99 52", a)
print(*a)

print("\nДевятнадцатое")

matrix = [[1, 2], [3, 4]]


def transpore(matr):
    global matrix
    result = [[0, 0], [0, 0]]  # Создаем новую матрицу для транспонирования
    for i in range(len(matr)):
        for j in range(len(matr[0])):
            result[j][i] = matr[i][j]  # Транспонируем значения
    matrix = result  # Присваиваем результат транспонирования обратно в глобальную переменную matrix


transpore(matrix)
for line in matrix:
    print(*line)

print("\nДвадцатое")


def swap():
    global first, second
    first[:], second[:] = second[:], first[:]


first = [1, 2, 3]
second = [4, 5, 6]

first_content = first[:]
second_content = second[:]

swap()
print(first, second_content, first == second_content)
print(second, first_content, second == first_content)

print("\nДвадцать первое")
fractal = [2, 5]


def defractalize():
    global fractal
    for i in fractal:
        if i == fractal:
            del fractal[fractal.index(i)]


fractal.append(fractal)
fractal.append(3)
fractal.append(fractal)
defractalize()
fractal.append(9)
print(fractal)

print("\nДвадцать второе")


def print_fractal():
    global fractal
    result = []
    for elem in fractal:
        if isinstance(elem, list):
            for sub_elem in elem:
                result.append(sub_elem)
    fractal = result


fractal = [3]
fractal.append(fractal)
fractal.append(2)

print_fractal()
print(fractal)

print("\nДвадцать третье")


def matrix(*args, **kwargs):
    if len(args) == 3:
        rows = [[args[2]] * args[0] for _ in range(args[1])]
        return rows
    elif len(args) == 2:
        rows = [[0] * args[0] for _ in range(args[1])]
        return rows
    elif len(args) == 1:
        rows = [[0] * args[0] for _ in range(args[0])]
        return rows
    return [0]


rows = matrix()
print("Матрица 1:")
for line in rows:
    if (len(rows) == 1):
        print(line)
        break
    print(*line)
print("Матрица 2:")
rows = matrix(2)
for line in rows:
    print(*line)
print("Матрица 3:")
rows = matrix(3, 5, 7)
for line in rows:
    print(*line)

print("\nДвадцать четвертое")


def partial_sum(*args):
    if len(args) == 1:
        return [0, args[0]]
    elif len(args) > 1:
        result = [0, args[0]]
        for i in range(1, len(args)):
            result.append(sum(args[0:i + 1]))
        return result
    return [0]


print(partial_sum(1, 0.5, 0.25, 0.125))

print("\nДвадцать пятое")

import math


def solve(*coefficients):
    if len(coefficients) == 0 or len(coefficients) > 3:
        return
    if all(i == 0 for i in coefficients):
        return ["all"]
    elif len(coefficients) == 3:
        if (coefficients[1] ** 2 - 4 * coefficients[0] * coefficients[2]) > 0:
            x1 = (-coefficients[1] - math.sqrt(coefficients[1] ** 2 - 4 * coefficients[0] * coefficients[2])) \
                 / 2 * coefficients[0]
            x2 = (-coefficients[1] + math.sqrt(coefficients[1] ** 2 - 4 * coefficients[0] * coefficients[2])) \
                 / 2 * coefficients[0]
            return [x1, x2]
        elif (coefficients[1] ** 2 - 4 * coefficients[0] * coefficients[2]) == 0:
            return [-coefficients[1] / 2 * coefficients[0]]
    elif len(coefficients) == 2:
        return [-coefficients[1] / coefficients[0]]
    elif len(coefficients) == 1:
        return [coefficients[0]]


print(solve(1, 5, 4))
