from abc import ABC, abstractmethod

# https://www.smartfile.com/blog/abstract-classes-in-python/
# https://ru.godaddy.com/engineering/2018/12/20/python-metaclasses/

# or interface
class AbstractClass(ABC):
    @abstractmethod
    def some_method(self):
        pass


class ImplementedClass(AbstractClass):
    def some_method(self):
        print("I'm implemented!")


# // raise TypeError
# abstract_obj = AbstractClass()
# abstract_obj.some_method()

implemented_obj = ImplementedClass()
implemented_obj.some_method()