from functools import reduce

# Первое
str1 = input("Введите название фильма: ")
str2 = input("Введите название кинотеатра: ")
str3 = input("Введите время начала сеанса: ")

print(f"Билет на {str1} в {str2} на {str3} забронирован.")


# Второе
# str1 = input("Введите первую строку: ")
# str2 = input("Введите вторую строку: ")
#
#
# def check_word(str, list_word):
#     if all(letter in str.lower() for letter in list_word):
#         return True
#     else:
#         return False
#
#
# if check_word(str1, ["н", "е", "т"]) and check_word(str2, ["н", "е", "т"]) \
#         or check_word(str1, ["д", "а"]) and check_word(str2, ["д", "а"]):
#     print("Верно")
# else:
#     print("Неверно")

# Третье

# if "@" not in input("Введите логин: ") and "@" in input("Введите адрес: "):
#     print("Верно введены данные")
# else:
#     print("Неверно введены данные")

# Четвертое

# print(input())


# Пятое

# str1 = input()
# if str1 == "":
#     print("ДА")
# else:
#     print("НЕТ")

# Шестое

# number = input()
# max_number = max(number[i] for i in range(0, len(number)))
# min_number = min(number[i] for i in range(0, len(number)))
# average_number = number.replace(max_number, "")
# average_number = average_number.replace(min_number, "")
#
# if (int(max_number) + int(min_number)) / 2 == int(average_number):
#     print("Вы ввели красивое число")
# else:
#     print("Жаль, вы ввели обычное число")

# Седьмое

# number = int(input("Введите четырехзначное число: "))
#
# num1 = number % 10
# num2 = (number // 10) % 10
# num3 = (number // 100) % 10
# num4 = number // 1000
#
# for i in sorted([num1, num2, num3, num4]):
#     print(i, end='')

# Восьмое

# l = []
# l_final = []
# value = ""
# while value != "!":
#     value = input()
#     l.append(value)
#     l_final.append(value)
# l.remove("!")
# l_final.remove("!")
# count = 0
# for i in range(0, len(l)):
#     if 150 < int(l[i]) < 190:
#         count += 1;
#     else:
#         l_final.remove(l[i])
# print(count)
# print(min(l_final), max(l_final))

# Девятое

# password1 = ""
# password2 = ""
#
# while True:
#     password1 = input("Введите пароль: ")
#     if len(password1) < 8 and "@" not in password1:
#         print("Короткий!")
#         continue
#     if "123" in password1:
#         print("Простой!")
#         continue
#
#     password2 = input("Повторите ввод пароля: ")
#
#     if password2 != password1:
#         print("Различаются!")
#         continue
#     else:
#         print("OK")
#         break

# Десятое

# while True:
#     value1 = int(input("Введите первое значение: "))
#     sign = input("Символ операции(+, -, *, /, %, !, x): ")
#     if sign == "!":
#         print(reduce(lambda x, y: x * y, [i for i in range(1, value1 + 1)]))
#         continue
#     elif sign == "x":
#         print(value1)
#         continue
#     value2 = int(input("Введите второе значение: "))
#     if sign in "+-*/%":
#         if sign == "+":
#             print("Ответ", value1 + value2)
#         elif sign == "-":
#             print("Ответ", value1 - value2)
#         elif sign == "*":
#             print("Ответ", value1 * value2)
#         elif sign == "/":
#             print("Ответ", value1 / value2)
#         elif sign == "%":
#             print("Ответ", value1 % value2)
#     else:
#         print("Вы ввели неверный символ операции")


# Одиннадцатое

# for i in range(n := int(input("num -->"))):
#     print(('*'*(2*i+1)).rjust(n + i))


# Двенадцатое
# a = 0
# b = 1
# for i in range(1, int(input("num -->")) + 1):
#     print(i, end=" ")
#     a += 1
#     if b == a:
#         print()
#         b += 1
#         a = 0


# Тринадцатое

# value1 = int(input())
# value2 = int(input())
# symbl = input()
#
# print(symbl * value2)
# for i in range(value1 - 2):
#     print(symbl, " " * (value2 - 4), symbl)
# print(symbl * value2)
