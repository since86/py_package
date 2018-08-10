class Student:
    name = None
    age = 18
    course = 'python'

    def doHomework(self):
        print(self.course)
        return None

eric = Student()
eric.doHomework()
print(type(eric))