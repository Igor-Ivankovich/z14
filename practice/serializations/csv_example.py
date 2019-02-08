file = open('example.csv')
data = file.read()
data = data.split('\n')
data = map(lambda x: x.split(','), data)
# print(list(data))
file.close()

file = open('example.csv')
data = file.readlines()
data = map(lambda x: x.split(','), data)
# print(list(data))
file.close()

file = open('example.csv')
data = file.readline()
result = []
while data:
    result.append(data[:-1].split(','))
    data = file.readline()
print(result)
file.close()

text_result = map(lambda x: ','.join(x), result)
text_result = '\n'.join(text_result)

file = open('new.csv', 'w')
file.write(text_result)
file.close()

print('#' * 100)
import csv

file = open('example.csv')
reader = csv.reader(file)
for line in reader:
    print(line[5])
file.close()

print('#' * 100)
file = open('example.csv')
reader = csv.DictReader(file)
for line in reader:
    print(dict(line))
    print(line['column3'])
print(reader.fieldnames)
file.close()

# WRITE
file = open('write.csv', 'w')
writer = csv.writer(file)
writer.writerow(['first_name', 'last_name'])
writer.writerows([['Tima', 'Akulich']])
file.close()

file = open('write1.csv', 'w')
writer = csv.DictWriter(file, fieldnames=['first', 'last'])
writer.writeheader()
writer.writerows([{'first': 'Tima', 'last': 'Akulich'}])
file.close()


