
class Person():
    name = 'noName'
    age = 18

    def eat(self):
        print('吃饭')

    def sleep(self):
        print('睡觉')


class Teacher(Person):
    def work(self):
        print('教学')

class Student(Person):
    def study(self):
        print('学习')

class Tutor(Teacher,Student):
    pass

t = Tutor()
print(t.__dict__)
print(Tutor.__dict__)
print(Tutor.__mro__)

print('*'*20)
#mixin
class TeacherMixin():
    def work(self):
        print('mixin教学')

class StudentMixin():
    def study(self):
        print('mixin学习')

class TutorM(Person,TeacherMixin,StudentMixin):
    pass

tt = TutorM()
print(tt.__dict__)
print(TutorM.__dict__)
print(TutorM.__mro__)