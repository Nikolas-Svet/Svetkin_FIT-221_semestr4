print("Первое")
string = "Hello, world!"
print(string[2], "Вывести третий элемент")
print(string[-2], "Вывести предпоследний символ")
print(string[0:5], "Первые пять символов")
print(string[:-2], "Все кроме двух последних")
print(string[0::2], "Четные символы")
print(string[1::2], "Нечетные")
print(string[-1::-1], "В обратном порядке")
print(string[-1::-2], "Через одного в обратном порядке")
print(len(string), "Вся длина")

print("\nВторое")

string2 = string[round(len(string) / 2):] + "__" + string[0:round(len(string) / 2)]
print(string2)

print("\nТретье")

string = "aaaaaahприветhsssssss"
h_start = string.index("h")
h_end = string[h_start + 1:].index("h") + h_start + 1
# + 1 потому что я вырезаю часть строки и подсчет идет с нуля и как раз ноль и создает недостающую единицу
print(string[h_start + 1:h_end])

print("\nЧетвертое")

string = "aafaafaafafffaa"

print("Первый:", string.index("f"), "\nПоследний", len(string) - (string[-1::-1].index("f") + 1))

print("\nПятое")

first_second_move = True
string1 = input()
string2 = input()
while True:
    if string1[-1] == string2[0] and first_second_move:
        string1 = input()
        first_second_move = False
        continue
    elif string2[-1] == string1[0] and not first_second_move:
        string2 = input()
        first_second_move = True
        continue
    else:
        print(string2 if first_second_move else string1)
        break

print("\nШестое")

string = input()
print(''.join([string[i] * (i + 1) for i in range(len(string))]))

print("\nСедьмое")

string = "@vvv>>>>>>>>v<<vvvv<<<vv>>>"
# string = ".>>>vv<<v"
for_rjust = 0
move_left = False
count_move_left = 1

if string[1] == ">":
    for_rjust += 1
    print(string[0], end="")
else:
    print(string[0], sep="")
i = 0
for i in range(1, len(string)):
    if move_left:
        if string[i] == "<" and i + 1 < len(string):
            count_move_left += 1
        else:
            if i == len(string) - 1:
                count_move_left += 1
            move_left = False
            print((string[0] * count_move_left).rjust(for_rjust))
            for_rjust = for_rjust + 1 - count_move_left
    if string[i] == ">":
        print(string[0], end="")
        for_rjust += 1
        if (i + 1 < len(string)) and string[i + 1] != ">":
            print()

    if string[i] == "v":
        if (i + 1 < len(string)) and string[i + 1] == "<":
            move_left = True
            continue
        if i + 1 < len(string) and string[i + 1] == ">":
            continue
        print((string[0]).rjust(for_rjust))

print("\nВосьмое")

string = "рогатка"
# string = "синхрофазотрон"
flag = True
if round(len(string) / 2) == (len(string) // 2):
    count = len(string) // 2
    string_1 = string[0:count][-1::-1]
    string_2 = string[count:]
else:
    count = round(len(string) / 2)
    string_1 = string[0:count][-1::-1]
    string_2 = string[count:]
count2 = 0
for i in range(max(round(len(string_1)), len(string_2))):
    if len(string_1) != len(string_2):
        if i == 0:
            print(string_1[i].rjust(count))
            count -= 1
            count2 += 1
            continue
        print(string_1[i].rjust(count), " " * count2, string_2[i - 1], sep="")
        count -= 1
        count2 += 2
        continue
    print(string_1[i].rjust(count), " " * count2, string_2[i], sep="")
    count -= 1
    count2 += 2

print("\nДевятое")

numbers = [5, 2, 4, 6, 7]

result = filter(lambda x: x[0] < x[1], zip(numbers[:-1], numbers[1:]))
# Благодаря функции zip, которая по очереди берет элементы из двух списков, создаются кортежи
# с парными числами, которые как раз-таки нам нужны для сравнения
# Функция оставляет все кортежи, где функция выводит True
print(" ".join([str(max(i)) for i in list(result)]))

print("\nОдиннадцатое")

a = [1, 4, 7, 2, 63, 53, 78, 32, 24]
for i in range(0, len(a), 2):
    if i == (len(a) - 1) and i % 2 == 0:
        break
    a[i], a[i + 1] = a[i + 1], a[i]
print(a)

print("\nДвенадцатое")

a = [1, 4, 7, 2, 63, 53, 78, 32, 24, 1, 4, 4, 333, 231, 111]

print(list(filter(lambda x: a.count(x) == 1, a)))

print("\nТринадцатое")

st = input("Введите строку: ").split(" ")
a = list(input().split(" "))
first_print = True
for i in a:
    if first_print:
        print(st[int(i) - 1][0].upper() + st[int(i) - 1][1:], end=" ")
        first_print = False
        continue
    print(str[int(i) - 1].lower(), end=" ")

print("\nЧетырнадцатое")


def are_queens_attacking(queens_def):
    for i in range(len(queens_def)):
        for j in range(i + 1, len(queens_def)):
            if queens_def[i][0] == queens_def[j][0] or queens_def[i][1] == queens_def[j][1] or abs(queens_def[i][0] - queens_def[j][0]) == abs(
                    queens_def[i][1] - queens_def[j][1]):
                return True
    return False


queens = []
for _ in range(8):
    x, y = map(int, input().split())
    queens.append((x, y))

if are_queens_attacking(queens):
    print("YES")
else:
    print("NO")

print("\nПятнадцатое")

n = int(input())
count = -1
array = []
while n > 0:
    s = input()
    if "Кто последний? Я" in s:
        array.append(s)
    elif "Следующий!" in s:
        if 0 == len(array):
            print("В очереди никого нет")
            continue
        if "Кто последний? Я - " in array[0]:
            print("Заходит", array[0][18:], "!", sep="")
        elif "Я только спросить! Я - " in array[0]:
            print("Заходит", array[0][22:], "!", sep="")
        del array[0]
    elif "Я только спросить!":
        array = [s] + array
    n -= 1
