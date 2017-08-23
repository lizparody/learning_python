class Calculator(object):
    def __init__(self):
        pass

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def subtract(cls, a, b):
        return cls.add(a, b * -1)

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        return a / b
