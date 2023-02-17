from datetime import datetime


def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result
    return wrapper


@timeit
def foo1(n):
    a = []
    for i in range(n):
        if i%2 == 0:
            a.append(i)
    return a


@timeit
def foo2(n):
    a = [i for i in range(n) if i%2 == 0]
    return a

a = timeit(foo1)(10) # wrapper(10) -> foo1(10) -> will be printed time and list [0, 2, 4, 6, 8]
print(a)

