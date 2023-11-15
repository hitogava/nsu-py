class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Singleton:
    instance = None
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.__init__(cls, *args[0])
            cls.__init__ = lambda *args: None
        return cls.instance

    def __init__(self, a, b):
        self.a = a
        self.b = b


class GlobalA(Singleton, A):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, args, kwargs)
