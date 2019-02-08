import pickle

data = pickle.dumps([1, 2, 3, 4])
print(data)
print(pickle.loads(data))


file = open('file_set.txt', 'wb')
pickle.dump({1, 2, 3, 4}, file)
file.close()

file = open('file_set.txt', 'rb')
print(pickle.load(file))
file.close()