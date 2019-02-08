file = open('../README.md')
text = file.readlines()
print(text[:2])
file.close()

file = open('text.txt', mode='w')
file.write('Text')
file.close()

file = open('text.txt', mode='w')
file.write('New Text')
file.close()

file = open('text.txt', mode='a')
file.write('\nNew Text 2')
file.close()


file = open('../README.md')
text = file.read()
file.seek(10)
text1 = file.read()
print(text[:10], text1[:10])
file.close()

# file = open('1.jpg')
# data = file.read()
# file.close()
# print(data[:20])
#
# file = open('1.jpg', 'rb')
# data = file.read()
# file.close()
# print(data[:20])
