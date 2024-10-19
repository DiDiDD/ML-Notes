from abc import ABC, abstractmethod


class MyClass(ABC):
    def __new__(cls, *args, **kwargs):
        '''
        The purpose of __new__() is to handle the creation of a new instance of a class.
        It is responsible for:
        1. Allocating memory for the new object.
        2. Returning a new instance of the class.
        __new__() is called before __init__(), and it can return an existing instance or a new one.
        '''
        return

    def __init__(self):
        super().__init__()
        return

    @abstractmethod
    def specific_function(self):
        pass

    def __len__(self):
        return

    @classmethod
    def class_method(cls):
        return

    @staticmethod
    def static_method():
        return
