import abc
from types import MethodType

class Human(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def smoking(self):
        pass

    @classmethod
    def drink(cls):
        pass

    @staticmethod
    def sleep():
        pass


class Chinese(Human):
    def smoking(self):
        print('no smoking')

    def drink(cls):
        print(cls.__dict__)

    def sleep(self):
        print('休息')

def cook(self):
    print('烹饪')


c = Chinese()
c.smoking()
cook('chinese')
c.cook = MethodType(cook,Chinese)
#Chinese.cook = cook
c.cook()


