import pickle

age = 22
with open(r'test02.txt', 'wb') as f:
    pickle.dump(age,f)

with open(r'test02.txt', 'rb') as f:
    a = pickle.load(f)
    print(a)