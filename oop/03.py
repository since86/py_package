class Person():
    name = 'noname'
    age = 18
    gender = '男'
    def _eat(self):
        print(self.age)

    def __init__(self):
        print('工作')

class Worker(Person):
    def __init__(self,salary):
        print('工作一天，收入{0}元'.format(salary))

class Teacher(Worker):
    pass

t = Teacher(100)

