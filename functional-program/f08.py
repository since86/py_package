import time

#def hello():
    #print('Hello World')

def printTime(f):
    def wrapper(*args, **kwargs):
        print('Time: '+time.ctime())
        return f(*args,**kwargs)
    return wrapper

@printTime
def hello():
    print('Hello World!')

hello()



