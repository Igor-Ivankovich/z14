a = int(input('N1 = '))
b = int(input('N2 = '))

result = a % b

print('Частное', a // b)

if not result:
    print('Делится')
else:
    print('Не делится', result)
