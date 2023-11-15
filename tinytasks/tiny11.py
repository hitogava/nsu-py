class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Singleton:
    instance = None
    def __new__(cls, *args, **kwargs):
        if Singleton.instance is None:
            Singleton.instance = super().__new__(cls)
            super().__init__(cls, *args[0])
        return Singleton.instance
    def __init__(self):
        pass


class GlobalA(Singleton, A):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, args, kwargs)
    def __init__(self, a, b):
        super().__init__()
