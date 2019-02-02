a = int(input('N1 = '))
b = int(input('N2 = '))
c = int(input('N3 = '))

_max = None

if a > b and a > c:
    _max = a
elif b > a and b > c:
    _max = b
else:
    _max = c

print('Max', _max)
