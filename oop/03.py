class Person():
    name = 'noname'
    age = 18
    gender = '男'
    def eat(self):
        print(self.age)

class Student(Person):
    def learn(self):
        print('学习')

    def eat(self):
        super().eat()
        print('补充营养')

eric = Student()
eric.eat()
eric.learn()