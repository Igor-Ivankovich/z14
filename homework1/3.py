number = int(input("Количество бит"))
choice = int(input("1 - B, 2 - kB"))

result = None
if choice == 1:
    result = number // 8
if choice == 2:
    result = number // (8 * 1024)

print(result)
