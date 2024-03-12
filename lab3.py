# print("\nПервое")
#
# print(len(set(input().split())))

print("\nВторое")

array1 = [1, 3, 5, 2, 1, 5, 6, 7, 4]
array2 = [3, 3, 5, 5, 1, 7, 6, 9, 2]
print(len(set(array1) & set(array2)))

print("\nТретье")

print(set(array1) & set(array2))

print("\nЧетвертое")

# arr = [int(num) for num in input().split()]
# a = set(filter(lambda x: arr.count(x) > 1, arr))
# b = set(arr) - a
# print("\nYES" * len(a))
# print("\nNO" * len(b))

print("\nПятое")

n = "5 \n Hello, World! \n My name is Nikita \n I am from Russia \n Nice to see you! \n Can I help you?"
sum_words = 0
print(n[1:])
num = n[0]
n = n[1:].split("\n")
for i in n:
    if i == " ":
        continue
    else:
        sum_words += len(i.split())

print("Сумма слов равна:", sum_words)

print("\nШестое")

n = "6 \n Иванов \n Петров \n Сидоров \n Петров \n Иванов \n Петров "
sm = 0
num = n[0]
n = n[1:].split("\n")
f = set(n)

for i in f:
    if i == " ":
        continue
    elif n.count(i) > 1:
        sm += n.count(i)
print(sm)

print("\nСедьмое")

n = "яблоко вишня малина черешня яблоко яблоко черешня помидор вишня"
n = n.split()
f = set(n)
for i in f:
    print(i, "встречается:", n.count(i))

print("\nВосьмое")

print("\nДевятое")

print("\nДесятое")
