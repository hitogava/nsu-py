class A:
    def __init__(self, a, b):
        if not Singleton.initialized:
            self.a = a
            self.b = b
            Singleton.initialized = True


class Singleton:
    original = None
    initialized = False

    def __new__(cls, *args, **kwargs):
        if Singleton.original is None:
            Singleton.original = object.__new__(cls)
            Singleton.original.__init__(*args[0])
        return Singleton.original


class GlobalA(Singleton, A):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, args, kwargs)
    def __init__(self, a,b):
        super().__init__(a, b)


ga1 = GlobalA(1,2)
print(ga1.a, ga1.b)
ga2 = GlobalA(3,4)
print(ga1.a, ga1.b, ga1 is ga2)
