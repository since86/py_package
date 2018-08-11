class Student:
    name = None
    age = 18
    course = 'python'

    def doHomework(self):
        print(self.course)
        return None

    def say(self):
        print(self.name)

    def teach(self,stu):
        print('{0}给{1}补习'.format(self.name,stu))
eric = Student()
eric.doHomework()
print(eric.name)

eric.name = 'eric'
print(Student.__dict__)
print(eric.__dict__)


eric.say()

print(eric.name)

eric.teach('lily')

for k,v in Student.__dict__.items():
    print(k,'--',v)
