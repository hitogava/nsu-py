def sum(x,y):
    return x+y
def specialize(f,*args, **kwargs):
    def foo(*fooargs):
        return f(*args,*fooargs, **kwargs)
    return foo
plus_one = specialize(sum,y=1)
print(plus_one(10))
just_two = specialize(sum,1,1)
print(just_two())
