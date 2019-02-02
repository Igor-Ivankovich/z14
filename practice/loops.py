# a = int(input("A= "))
# b = int(input("B= "))
a = 1
b = 2

if a > b:
    pass
elif a == b:
    print("A == B")
elif a == 2:
    print("A == 2")
else:
    print("A < B")


if a % b == 0:
    print("Here")

##############################################
a = 'str1'
b = 'str2'
value = True

number = a if value else b

if value:
    number = a
else:
    number = b

###################################
# циклы
print('Циклы')
i = 10
while i:
    print(i)
    i -= 1
    if i == 5:
        break
else:
    print('Else')

for i in [1, 2, 3, 4, 5]:
    if i == 3:
        break
    if i == 2:
        continue
else:
    print('Else')

_list = [4, 3, 10, 21, 44]
_max = _list[0]
for item in _list:
    if item > _max:
        _max = item

print('Max', _max)  # asdfghjksasfghjklasdasdasdasdasdasdasdasdasd

# Заполнить массив вещественных чисел
# вводом с клавиатуры. Посчитать
# сумму и произведение элементов
# массива. Вывести на экран сам массив,
# полученные сумму и произведение его
# элементов.

_list = [1, 2, 3, 4, 5, 6, 7]

_sum = 0
_mul = 1
for item in _list:
    if not item % 2:
        _sum += item
        _mul *= item
print('Task', _sum, _mul)
