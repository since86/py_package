def gen():
    for c in 'ABc':
        yield c

def genf():
    yield from 'ABc'

if __name__ == '__main__':
    print(list(gen()))
    print(list(genf()))